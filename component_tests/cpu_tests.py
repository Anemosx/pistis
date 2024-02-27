import cpuinfo
import psutil
import platform


def run_cpu_tests():
    """
    Execute and display a series of CPU tests and related information.

    This function utilizes the `psutil`, `platform`, and `py-cpuinfo` libraries to gather and
    display comprehensive details about the system's CPU. It prints out an ASCII art header,
    followed by general CPU information and detailed specifications from the `py-cpuinfo` library.

    Parameters
    ----------
    None

    Returns
    -------
    None

    See Also
    --------
    psutil : Python library used to access system details and process utilities.
    platform : Provides access to underlying platform's identifying data.
    cpuinfo : Gathers CPU info from different sources.

    Notes
    -----
    The function begins by displaying an ASCII art banner followed by CPU information obtained
    through `psutil` and `platform` libraries, such as the number of physical and logical cores and
    the processor information. Subsequently, it provides a detailed account of the CPU
    characteristics using the `cpuinfo` library, which includes data on architecture, vendor, cache
    size, and frequencies.
    """

    print("=" * 50)

    print("       ____ ____  _   _")
    print("      / ___|  _ \| | | |")
    print("     | |   | |_) | | | |")
    print("     | |___|  __/| |_| |")
    print("      \____|_|    \___/")

    print("=" * 50)

    print("\npsutil\n")

    print("\t" + "-" * 25)

    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)

    cpu_info_processor = platform.processor()

    print(f"\tProcessor Info: {cpu_info_processor}")
    print(f"\tPhysical cores: {physical_cores}")
    print(f"\tLogical cores: {logical_cores}")

    print("\t" + "-" * 25)

    detailed_cpu_info = cpuinfo.get_cpu_info()
    cpuinfo_version = detailed_cpu_info["cpuinfo_version_string"]
    arch = detailed_cpu_info["arch"]
    arch_string_raw = detailed_cpu_info["arch_string_raw"]
    vendor_id_raw = detailed_cpu_info["vendor_id_raw"]
    brand_raw = detailed_cpu_info["brand_raw"]
    hz_actual_friendly = detailed_cpu_info["hz_actual_friendly"]
    hz_actual = detailed_cpu_info["hz_actual"]
    l2_cache_size = detailed_cpu_info["l2_cache_size"]
    family = detailed_cpu_info["family"]
    model = detailed_cpu_info["model"]
    l3_cache_size = detailed_cpu_info["l3_cache_size"]
    l2_cache_line_size = detailed_cpu_info["l2_cache_line_size"]
    l2_cache_associativity = detailed_cpu_info["l2_cache_associativity"]
    num_cores = detailed_cpu_info["count"]

    print(f"\npy-cpuinfo Version: {cpuinfo_version}\n")

    print("\t" + "-" * 25)

    print(f"\tCPU: {brand_raw}")
    print(f"\tLogical cores: {num_cores}")
    print(f"\tHz: {hz_actual_friendly}, {hz_actual}")
    print(
        f"\tVendor: {vendor_id_raw} Family: {family} Model: {model} Arch: {arch_string_raw}, {arch}"
    )
    print(
        f"\tL2 Cache: {l2_cache_size} Line Size: {l2_cache_line_size} Associativity {l2_cache_associativity}"
    )
    print(f"\tL3 Cache: {l3_cache_size}")

    print("\t" + "-" * 25)
    print()
