import psutil


def run_disk_tests():
    """
    Execute and display disk usage statistics for all mounted partitions.

    This function employs the `psutil` library to fetch and display disk partition information
    and usage statistics, such as total size, used space, free space, and usage percentage
    for each partition.

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
    The function prints an ASCII art banner followed by the disk information. For each partition
    detected using `psutil.disk_partitions()`, it displays the device name, mountpoint, file system
    type, and usage statistics including total size, used space, free space, and the percentage used.
    In case the function lacks the necessary permissions to access any partition's information, it
    will indicate that the statistics could not be accessed.
    """

    print("=" * 50)

    print("      ____ ___ ____  _  __")
    print("     |  _ \_ _/ ___|| |/ /")
    print("     | | | | |\___ \| ' / ")
    print("     | |_| | | ___) | . \ ")
    print("     |____/___|____/|_|\_\\")

    print("=" * 50)

    print("\npsutil\n")

    print("\t" + "-" * 25)
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"\tDevice: {partition.device}")
        print(f"\t\tMountpoint: {partition.mountpoint}")
        print(f"\t\tFile system type: {partition.fstype}")
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"\t\tTotal Size: {usage.total / (2 ** 30):.2f} GiB")
            print(f"\t\tFree: {usage.free / (2 ** 30):.2f} GiB")
            print(f"\t\tUsed: {usage.used / (2 ** 30):.2f} GiB")
            print(f"\t\tPercentage: {usage.percent}%")
        except PermissionError:
            print(f"\t\tCould not access statistics for {partition.mountpoint}")
        print()

    print("\t" + "-" * 25)
    print()
