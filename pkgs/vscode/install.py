from arch.lib.package_manager import get_package_manager



def install():
    get_package_manager().install("code")
