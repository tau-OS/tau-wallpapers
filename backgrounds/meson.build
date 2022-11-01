dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'tau-light.png',
  'tau-dark.png',
  'neutrino-dark.png',
  'neutrino-light.png',
  '3D_01.png',
  'bradley-allweil.jpg',
  'daniel-sessler.jpg',
  'giordano-rossoni.jpg',
  'jan-walter-luigi.jpg',
  'luka-verc.jpg',
  'simon-berger.jpg'
]

install_data(backgrounds, install_dir: backgrounddir)

foreach metadata : [
  'backgrounds.xml',
  'tau.xml',
  'neutrino.xml']
  configure_file(
    input: metadata + '.in',
    output: metadata,
    configuration: dataconf,
    install: true,
    install_dir: metadatadir
  )
endforeach

