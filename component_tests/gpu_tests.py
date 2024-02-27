import GPUtil
import torch
from pycuda import driver as cuda_driver


def run_gpu_tests():
    """
    Execute and display GPU memory and usage statistics using Torch, GPUtil and PyCUDA.

    This function utilizes the `torch`, `GPUtil` and `PyCUDA` libraries to fetch and
    display GPU information and memory usage statistics. It provides details such as
    the CUDA version, GPU device names, total VRAM, free VRAM, and allocated VRAM.

    Parameters
    ----------
    None

    Returns
    -------
    None

    See Also
    --------
    torch : Library for accessing Torch CUDA information.
    GPUtil : Library used to get GPU status from NVIDIA GPUs using nvidia-smi.
    PyCUDA : Module to interact with CUDA, providing GPU memory information.

    Notes
    -----
    The function begins by displaying GPU information using Torch, if CUDA is available,
    including the CUDA version, device name, and memory details. It then uses GPUtil to
    provide a broader set of GPU information for NVIDIA GPUs. Finally, it leverages PyCUDA
    to get detailed memory statistics. For each GPU detected, it prints details like the
    GPU ID, name, total VRAM, free VRAM, and used VRAM. If CUDA is not available, it
    indicates that Torch CUDA is not accessible.
    """

    print("=" * 50)

    print("   ____ ____  _   _ ")
    print("  / ___|  _ \| | | |")
    print(" | |  _| |_) | | | |")
    print(" | |_| |  __/| |_| |")
    print("  \____|_|    \___/ ")

    print("=" * 50)

    print("\nTorch CUDA\n")

    print("\t" + "-" * 25)

    if torch.cuda.is_available():
        print(f"\tVersion: {torch.version.cuda}")

        device_name = torch.cuda.get_device_name(torch.cuda.current_device())
        print(f"\tGPU Device Name: {device_name}")

        cuda_idx = torch.cuda.current_device()
        total_memory = torch.cuda.get_device_properties(cuda_idx).total_memory / (
            1024**2
        )
        allocated_memory = torch.cuda.memory_allocated(cuda_idx) / (1024**2)
        free_memory = total_memory - allocated_memory

        print(f"\tTotal VRAM: {total_memory:.2f} MB")
        print(f"\tFree VRAM: {free_memory:.2f} MB")
        print(f"\tAllocated VRAM: {allocated_memory:.2f} MB")

    else:
        print("\tNo Torch CUDA available")

    print("\t" + "-" * 25)

    gpus = GPUtil.getGPUs()

    for gpu in gpus:
        print("\nGPUtil\n")
        print("\t" + "-" * 25)

        print(f"\tGPU ID: {gpu.id}, \t Name: {gpu.name}")
        print(f"\tTotal VRAM: {gpu.memoryTotal} MB")
        print(f"\tFree VRAM: {gpu.memoryFree} MB")
        print(f"\tUsed VRAM: {gpu.memoryUsed} MB")
        print("\t" + "-" * 25)

        print("\nPyCUDA\n")
        print("\t" + "-" * 25)

        device = cuda_driver.Device(gpu.id)
        context = device.make_context()
        free, total = cuda_driver.mem_get_info()
        print(f"\tTotal VRAM: {device.total_memory() // (1024 ** 2)} MB")
        print(f"\tFree VRAM: {free // (1024 ** 2)} MB")
        print(f"\tUsed VRAM: {(total - free) // (1024 ** 2)} MB")
        context.pop()

        print("\t" + "-" * 25)
