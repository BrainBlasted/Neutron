# Neutron Story Progression

Neutron is a trait-based story progression mod for The Sims 4. It aims to create stories
for NPCs in a way that fits with their personalities and situations.

# Contributing

To get started with contributing to Neutron, please start by reading the [design document](./DESIGN.md).
This gives an overview of the core goals of Neutron as a story progression mod. Once done, you'll need to
set up a Python workspace. I recommend [this workspace for modding The Sims 4](https://sims4studio.com/thread/15145/started-python-scripting)
by andrew. I also recommend editing the `compile_module()` function in in `__init__.py` and `compiler.py` to the following:

```python
def compile_module(creator_name, root, mods_folder, mod_name=None, use_creator_name=True):
    src = os.path.join(root, 'Scripts')
    if not mod_name:
        mod_name=os.path.basename(os.path.normpath(os.path.dirname(os.path.realpath('__file__'))))

    if use_creator_name:
        mod_name = creator_name + '_' + mod_name
    ts4script = os.path.join(root, mod_name + '.ts4script')

    ts4script_mods = os.path.join(os.path.join(mods_folder), mod_name + '.ts4script')

    zf = PyZipFile(ts4script, mode='w', compression=ZIP_STORED, allowZip64=True, optimize=2)
    for folder, subs, files in os.walk(src):
        zf.writepy(folder)
    zf.close()
    shutil.copyfile(ts4script, ts4script_mods)
```

Once this change is made, rename the checkout of Neutron to "My Script Mods",
and replace the existing "My Script Mods" folder.

If you want PyCharm to be able to auto-fill and handle imports between modules,
you'll need to add the "Scripts" folder of each module as a source within your
workspace settings.

# License

Neutron is licensed under the Creative Commons Zero public domain license. You can re-use all code within this mod
for your own modifications or for any other purpose.

[![License: CC0-1.0](https://licensebuttons.net/l/zero/1.0/80x15.png)](http://creativecommons.org/publicdomain/zero/1.0/)