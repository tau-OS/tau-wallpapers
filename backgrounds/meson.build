dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'tau-light.png',
  'tau-dark.png',
  'neutrino-dark.png',
  'neutrino-light.png',
  '3D_01-light.png',
  '3D_01-dark.png',
  'ally-griffin.jpg',
  'and-machines-light.jpg',
  'and-machines-dark.jpg',
  'bradley-allweil.jpg',
  'daniel-sessler.jpg',
  'dim-gunger-light.jpg',
  'dim-gunger-dark.jpg',
  'fakurian-design-light.jpg',
  'fakurian-design-dark.jpg',
  'giordano-rossoni.jpg',
  'jan-walter-luigi.jpg',
  'john-paul-dorf.jpg',  
  'luka-verc.jpg',
  'marek-piwnicki-light.jpg',
  'marek-piwnicki-dark.jpg',
  'maxim-berg-light.jpg',
  'maxim-berg-dark.jpg',
  'simon-berger.jpg',
  'solen-feyissa-light.jpg',
  'solen-feyissa-dark.jpg',
  'warren-umoh-light.jpg',
  'warren-umoh-dark.jpg'
]

install_data(backgrounds, install_dir: backgrounddir)

foreach metadata : [
  'backgrounds.xml',
  'tau.xml',
  'neutrino.xml',
  'fakurian-design.xml',
  'maxim-berg.xml',
  '3D_01.xml',
  'and-machines.xml',
  'dim-gunger.xml',
  'marek-piwnicki.xml',
  'solen-feyissa.xml',
  'warren-umoh.xml']
  configure_file(
    input: metadata + '.in',
    output: metadata,
    configuration: dataconf,
    install: true,
    install_dir: metadatadir
  )
endforeach

