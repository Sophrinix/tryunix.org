from setuptools import setup, find_packages

setup(
        name = "TryUnix.org",
        version = "0.1",
        description = "Try Unix in a Browser",
        url = 'http://tryunix.org',
        author = "Alexandre Gauthier",
        author_email = "alex@lab.underwares.org",
        license = "MIT",
        packages = find_packages(),
        include_package_data = False,
        zip_safe = False,
        
        install_requires = [
                'WebCore', 'Genshi', 'Beaker'
            ],

        paster_plugins = ['PasteScript', 'WebCore']
    )
