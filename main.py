from component_tests.cpu_tests import run_cpu_tests
from component_tests.disk_tests import run_disk_tests
from component_tests.gpu_tests import run_gpu_tests
from component_tests.memory_tests import run_memory_tests


def run_tests():
    run_cpu_tests()
    run_memory_tests()
    run_disk_tests()
    run_gpu_tests()


if __name__ == "__main__":
    run_tests()
