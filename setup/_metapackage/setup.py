import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-akretion-sped-extractor",
    description="Meta package for akretion-sped-extractor Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-l10n_br_spec_sped',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 10.0',
    ]
)
