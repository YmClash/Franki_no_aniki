import torch
import os
from  torchvision import datasets
from PIL import Image
from torch import nn, load
from torch.optim import Adam
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms import Compose, ToTensor, Lambda


class CustomDataset(Dataset) :
    def __init__(self, root_dir, transform=None) :
        self.root_dir = root_dir
        self.transform = transform
        self.image_files = [f for f in os.listdir(root_dir) if f.endswith('.jpg')]

    def __len__(self) :
        return len(self.image_files)

    def __getitem__(self, idx) :
        img_path = os.path.join(self.root_dir, self.image_files[idx])
        image = Image.open(img_path)
        image_name = self.image_files[idx]
        label = int(image_name.split('_')[3].split('.')[
                        0])  # Remplacez cette ligne par la logique pour obtenir l'étiquette correspondant à l'image. Cela dépendra de la façon dont votre dataset est structuré.

        if self.transform :
            image = self.transform(image)

        return image, label


def gray_to_rgb(image) :
    return image.convert("RGB")


transform = Compose([
    Lambda(gray_to_rgb),
    ToTensor()
])


train = datasets.MNIST(root="data_2",
                       download=True,
                       train=True,
                       transform=ToTensor(),
                       )
train_data = CustomDataset(root_dir='images/dataset',
                           transform=ToTensor(),
                           )
test_Train_data = datasets.MNIST(root="data_2",
                           train=False,
                           download=True,
                           transform=ToTensor(),
                           )
dataset = DataLoader(train, 32)
dataset_2 = DataLoader(train_data, batch_size=20, shuffle=True)


def get_output_size(input_size, kernel_size, stride=1, padding=0) :
    return (input_size - kernel_size + 2 * padding) // stride + 1


input_size = 28
output_size = get_output_size(input_size, kernel_size=3)  # Conv1
output_size = get_output_size(output_size, kernel_size=3)  # Conv2
output_size = get_output_size(output_size, kernel_size=5)  # Conv3
output_size = get_output_size(output_size, kernel_size=5)  # Conv4

print(f"Output size after conv layers: {output_size}")


class reseau_Neurone(nn.Module) :
    def __init__(self) :
        super(reseau_Neurone, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3)
        self.conv3 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5)
        self.conv4 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=5)

        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(64 * 16 * 16, 128)
        self.fc2 = nn.Linear(128, 10)  # Correction ici

    def forward(self, x) :
        x = nn.ReLU()(self.conv1(x))
        x = nn.ReLU()(self.conv2(x))
        x = nn.ReLU()(self.conv3(x))
        x = nn.ReLU()(self.conv4(x))

        x = self.flatten(x)
        x = nn.ReLU()(self.fc1(x))
        x = self.fc2(x)
        return x


classeur_image = reseau_Neurone().to('cpu')
optimiseur = Adam(classeur_image.parameters(), lr=1e-3)
perte_fonction = nn.CrossEntropyLoss()

num_epoch = 300
for epoch in range(num_epoch) :
    for batch in dataset_2 :
        x, y = batch
        x, y = x.to('cpu'), y.to('cpu')
        yhat = classeur_image(x)
        perte = perte_fonction(yhat, y)

        optimiseur.zero_grad()
        perte.backward()
        optimiseur.step()
    print(F'epoch : {epoch}  pert est : {perte}')

with open('numb_model_3.pt', 'wb') as f :
    torch.save(classeur_image.state_dict(), f)

with open('numb_model_3.pt','rb') as f:
    classeur_image.load_state_dict(load(f))

img0 = Image.open('images/testset/0_9.jpg')
# img1 = Image.open('images/testset/1_8.jpg')
# img2 = Image.open('images/testset/2_7.jpg')
# img3 = Image.open('images/testset/3_6.jpg')
# img4 = Image.open('images/testset/4_5.jpg')
# img5 = Image.open('images/testset/6_4.jpg')
# img6 = Image.open('images/testset/7_3.jpg')
# img7 = Image.open('images/testset/8_2.jpg')
# img8 = Image.open('images/testset/9_1.jpg')
# img9 = Image.open('images/testset/10_0.jpg')



img_tensor0 = ToTensor()(img0).unsqueeze(0).to('cpu')

# img_tensor1 = ToTensor()(img1).unsqueeze(0).to('cpu')
#
# img_tensor2 = ToTensor()(img2).unsqueeze(0).to('cpu')
#
# img_tensor3 = ToTensor()(img3).unsqueeze(0).to('cpu')
#
# img_tensor4 = ToTensor()(img4).unsqueeze(0).to('cpu')
#
# img_tensor5 = ToTensor()(img5).unsqueeze(0).to('cpu')
#
# img_tensor6 = ToTensor()(img6).unsqueeze(0).to('cpu')
#
# img_tensor7 = ToTensor()(img7).unsqueeze(0).to('cpu')
#
# img_tensor8 = ToTensor()(img8).unsqueeze(0).to('cpu')
#
# img_tensor9 = ToTensor()(img9).unsqueeze(0).to('cpu')



print(f'le resultat du test est : ')

# print(torch.argmax(classeur_image(img_tensor0)))

print(f'resulat img_0 Tensor: {torch.argmax(classeur_image(img_tensor0))},la reponse est : 9 ')
if torch.argmax((classeur_image(img_tensor0))) == 9:
    print('vrai')
else:
    print('Faux')

# print(f'resulat img_1 Tensor: {torch.argmax(classeur_image(img_tensor1))},la reponse est : 8 ')
# if torch.argmax((classeur_image(img_tensor0))) == 8:
#     print('vrai')
# else:
#     print('Faux')
#
# print(f'resulat img_2 Tensor: {torch.argmax(classeur_image(img_tensor2))},la reponse est : 7 ')
# if torch.argmax((classeur_image(img_tensor0))) == 7:
#     print('vrai')
# else:
#     print('Faux')
#
# print(f'resulat img_3 Tensor: {torch.argmax(classeur_image(img_tensor3))},la reponse est : 6 ')
# if torch.argmax((classeur_image(img_tensor0))) == 6:
#     print('vrai')
# else:
#     print('Faux')
#
# print(f'resulat img_4 Tensor: {torch.argmax(classeur_image(img_tensor4))},la reponse est : 5')
# if torch.argmax((classeur_image(img_tensor0))) == 5:
#     print('vrai')
# else:
#     print('Faux')
#
# print(f'resulat img_5 Tensor: {torch.argmax(classeur_image(img_tensor5))},la reponse est : 4 ')
# if torch.argmax((classeur_image(img_tensor0))) == 4:
#     print('vrai')
# else:
#     print('Faux')
#
# print(f'resulat img_6 Tensor: {torch.argmax(classeur_image(img_tensor6))},la reponse est : 3 ')
# if torch.argmax((classeur_image(img_tensor0))) == 3:
#     print('vrai')
# else:
#     print('Faux')
#
# print(f'resulat img_7 Tensor: {torch.argmax(classeur_image(img_tensor7))},la reponse est : 2 ')
# if torch.argmax((classeur_image(img_tensor0))) == 2:
#     print('vrai')
# else:
#     print('Faux')
#
# print(f'resulat img_8 Tensor: {torch.argmax(classeur_image(img_tensor8))},la reponse est : 1 ')
# if torch.argmax((classeur_image(img_tensor0))) == 1:
#     print('vrai')
# else:
#     print('Faux')
#
# print(f'resulat img_9 Tensor: {torch.argmax(classeur_image(img_tensor9))},la reponse est : 0 ')
# if torch.argmax((classeur_image(img_tensor0))) == 0:
#     print('vrai')
# else:
#     print('Faux')
#
