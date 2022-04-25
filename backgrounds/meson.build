dataconf = configuration_data()
dataconf.set('BACKGROUNDDIR', backgrounddir)
dataconf.set('datadir', datadir)

backgrounds = [
  'tau-light.png',
  'tau-dark.png',
  '3D_01.png',
  'ally-griffin.jpg',
  'and-machines.jpg',
  'bradley-allweil.jpg',
  'daniel-sessler.jpg',
  'dim-gunger.jpg',
  'fakurian-design.jpg',
  'giordano-rossoni.jpg',
  'jan-walter-luigi.jpg',
  'john-paul-dorf.jpg',  
  'luka-verc.jpg',
  'marek-piwnicki.jpg',
  'maxim-berg.jpg',
  'simon-berger.jpg',
  'solen-feyissa.jpg',
  'warren-umoh.jpg',
]

install_data(backgrounds, install_dir: backgrounddir)

foreach metadata : [
  'tau.xml',
  'tau-backgrounds.xml']
  configure_file(
    input: metadata + '.in',
    output: metadata,
    configuration: dataconf,
    install: true,
    install_dir: metadatadir
  )
endforeach

