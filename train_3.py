


def get_output_size(input_size, kernel_size, stride=1, padding=0) :
    return (input_size - kernel_size + 2 * padding) // stride + 1



input_size = 128
output_size = get_output_size(input_size, kernel_size=3)  # Conv1
print(f"Output size after conv layers: {output_size}")
output_size = get_output_size(output_size, kernel_size=3)  # Conv2
print(f"Output size after conv layers: {output_size}")
output_size = get_output_size(output_size, kernel_size=5)  # Conv3
print(f"Output size after conv layers: {output_size}")
output_size = get_output_size(output_size, kernel_size=5)  # Conv4
print(f"Output size after conv layers: {output_size}")


print(f"Output size after conv layers: {output_size}")