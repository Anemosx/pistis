import psutil


def run_memory_tests():
    """
    Execute and display system memory statistics using the psutil library.

    This function uses `psutil` to fetch and display the system's virtual memory
    statistics, including the total RAM available on the system.

    Parameters
    ----------
    None

    Returns
    -------
    None

    See Also
    --------
    psutil : Python library used to access system details and process utilities.

    Notes
    -----
    The function prints a header for memory tests followed by fetching and displaying
    the total available RAM using `psutil.virtual_memory()`. The memory information
    is presented in gigabytes for easy comprehension.
    """

    print("=" * 50)

    print("      ____      _    __  __")
    print("     |  _ \    / \  |  \/  |")
    print("     | |_) |  / _ \ | |\/| |")
    print("     |  _ <  / ___ \| |  | |")
    print("     |_| \_\/_/   \_\_|  |_|")

    print("=" * 50)

    print("\npsutil\n")

    mem_info = psutil.virtual_memory()

    print("\t" + "-" * 25)

    print(f"\tTotal RAM: {mem_info.total / (1024 ** 3):.2f} GB")

    print("\t" + "-" * 25)
    print()
