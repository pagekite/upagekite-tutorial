# Submodules

These are external projects which we rely on.

Fetch/update external project code:

    git submodule init
    git submodule update


Change to a different version of a submodule:

    cd submodules/project/

    # Note: Instead of v1.234 (a tag?) you can also pull a specific
    #       commit, or a branch (such as main).
    #
    git pull origin v1.234
    git checkout v1.234

    cd ..
    git add project
    git commit -m 'Move submodule/project to v1.234'


To add a new external project:

    cd submodules/
    git submodule add https://github.com/team/project-name
    git commit -m 'Added new submodule team/project-name'

    # Finally, edit your `sys_path_helper.py` to add the project
    # to sys.path, if you need to load its code as a module.
    vi app/sys_module_helper.py

