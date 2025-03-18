def get_or_install_and_setup(*package_groups: list[str | object] | object | str):
    def one(p: object | str):
        if 'p has get()':
            'p.get()' 
        elif 'p is str':
            'lib.get_package_manager.install(p)'
        elif 'p has pkg_name':
            'lib.get_package_manager.install(p.pkg_name)'

        if 'p has setup()':
            pass

    for pg in package_groups:
        if 'pg is itarble':
            for p in pg:
                one(p)
        else:
            one(p)


get_or_install_and_setup(
    pacman,
    base_pkg_names,
    rustup,
    paru,
    [vscode, terminus_font]
)