import os
import django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from autoslug import AutoSlugField
from nucleo.models import Tag, ZonaPais, Pais, Estado, Ciudad, Region, Ubicacion, Institucion, Dependencia, \
    Departamento, User, Programa, AreaConocimiento, AreaWOS, AreaEspecialidad, ImpactoSocial, Cargo, \
    FinanciamientoUNAM, FinanciamientoExterno, Metodologia, Beca, Tesis, ProgramaLicenciatura, \
    ProgramaMaestria, ProgramaDoctorado, ProgramaEspecializacion, TipoEvento, Evento, Proyecto
from apoyo_institucional.models import Actividad, Comision, Representacion, CargoAcademicoAdministrativo, \
    RepresentanteAnteOrganoColegiado, ComisionAcademica, ApoyoTecnico, ApoyoOtraActividad
from desarrollo_tecnologico.models import TipoDesarrollo, Licencia, DesarrolloTecnologico
from difusion_cientifica.models import MemoriaInExtenso, PrologoLibro, Resena, OrganizacionEventoAcademico, \
    ParticipacionEventoAcademico

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SIC.settings")

django.setup()


Zonas = ('América del Norte', 'América Central', 'América del Sur', 'Antillas', 'Europa', 'Asia', 'Europa-Asia',
         'África', 'Oceanía', 'Oceano Atlántico')

for i in Zonas:
    print(i)
    z = ZonaPais(zona=i)
    z.save()


Paises = (('México', 'Estados Unidos Mexicanos', 'MX', 1),
          ('Abjasia', 'República de Abjasia', 'AB', 6),
          ('Acrotiri y Dhekelia', 'Bases Soberanas de Acrotiri y Dhekelia', 'QM', 5),
          ('Afganistán', 'República Islámica de Afganistán', 'AF', 6),
          ('Albania', 'República de Albania', 'AL', 5),
          ('Alemania', 'República Federal de Alemania', 'DE', 5),
          ('Andorra', 'Principado de Andorra', 'AD', 5),
          ('Angola', 'República de Angola', 'AO', 8),
          ('Anguila', 'Anguila', 'AI', 2),
          ('Antigua y Barbuda', 'Antigua y Barbuda', 'AG', 4),
          ('Arabia Saudita', 'Reino de Arabia Saudita', 'SA', 6),
          ('Argelia', 'República Argelina Democrática y Popular', 'DZ', 8),
          ('Argentina', 'República Argentina', 'AR', 3),
          ('Armenia', 'República de Armenia', 'AM', 6),
          ('Aruba', 'Aruba', 'AW', 2),
          ('Australia', 'Mancomunidad de Australia', 'AU', 9),
          ('Austria', 'República de Austria', 'AT', 5),
          ('Azawad', 'Estado Independiente del Azawad', '00', 8),
          ('Azerbaiyán', 'República de Azerbaiyán', 'AZ', 6),
          ('Bahamas', 'Mancomunidad de las Bahamas', 'BS', 4),
          ('Bangladés', 'República Popular de Bangladesh', 'BD', 6),
          ('Barbados', 'Barbados', 'BB', 2),
          ('Baréin', 'Reino de Baréin', 'BH', 6),
          ('Bélgica', 'Reino de Bélgica', 'BE', 5),
          ('Belice', 'Belice', 'BZ', 2),
          ('Benín', 'República de Benín', 'BJ', 8),
          ('Bermudas', 'Bermudas', 'BM', 1),
          ('Bielorrusia', 'República de Bielorrusia', 'BY', 5),
          ('Birmania', 'Unión de Myanmar (antes Birmania)', 'MM', 6),
          ('Bolivia', 'Estado Plurinacional de Bolivia', 'BO', 3),
          ('Bosnia y Herzegovina', 'Bosnia y Herzegovina', 'BA', 5),
          ('Botsuana', 'República de Botsuana', 'BW', 8),
          ('Brasil', 'República Federativa del Brasil', 'BR', 3),
          ('Brunéi', 'Estado de Brunéi, Morada de la Paz', 'BN', 6),
          ('Bulgaria', 'República de Bulgaria', 'BG', 5),
          ('Burkina Faso', 'Burkina Faso (antes Republica del Alto Volta)', 'BF', 8),
          ('Burundi', 'República de Burundi', 'BI', 8),
          ('Bután', 'Reino de Bután', 'BT', 6),
          ('Cabo Verde', 'República de Cabo Verde', 'CV', 8),
          ('Camboya', 'Reino de Camboya', 'KH', 6),
          ('Camerún', 'República de Camerún', 'CM', 8),
          ('Canadá', 'Canadá', 'CA', 1),
          ('Catar', 'Estado de Catar', 'QA', 6),
          ('Chad', 'República del Chad', 'TD', 8),
          ('Chile', 'República de Chile', 'CL', 3),
          ('China', 'República Popular China', 'CN', 6),
          ('Chipre', 'República de Chipre', 'CY', 7),
          ('Ciudad del Vaticano', 'Estado de la Ciudad del Vaticano', 'VA', 5),
          ('Colombia', 'República de Colombia', 'CO', 3),
          ('Comoras', 'Unión de las Comoras', 'KM', 8),
          ('Corea del Norte', 'República Popular Democrática de Corea', 'KP', 6),
          ('Corea del Sur', 'República de Corea', 'KR', 6),
          ('Costa de Marfil', 'República de Costa de Marfil', 'CI', 8),
          ('Costa Rica', 'República de Costa Rica', 'CR', 2),
          ('Croacia', 'República de Croacia', 'HR', 5),
          ('Cuba', 'República de Cuba', 'CU', 4),
          ('Curazao', 'Curazao', 'CW', 2),
          ('Dinamarca', 'Reino de Dinamarca', 'DK', 5),
          ('Dominica', 'Mancomunidad de Dominica', 'DM', 4),
          ('Ecuador', 'República del Ecuador', 'EC', 3),
          ('Egipto', 'República Árabe de Egipto', 'EG', 8),
          ('El Salvador', 'República de El Salvador', 'SV', 2),
          ('Emiratos Árabes Unidos', 'Emiratos Árabes Unidos', 'AE', 6),
          ('Eritrea', 'Estado de Eritrea', 'ER', 8),
          ('Eslovaquia', 'República de Eslovaquia', 'SK', 5),
          ('Eslovenia', 'República de Eslovenia', 'SI', 5),
          ('España', 'Reino de España', 'ES', 5),
          ('Estados Unidos de América', 'Estados Unidos de América', 'US', 1),
          ('Estonia', 'República de Estonia', 'EE', 5),
          ('Etiopía', 'República Democrática Federal de Etiopía', 'ET', 8),
          ('Filipinas', 'República de las Filipinas', 'PH', 6),
          ('Finlandia', 'República de Finlandia', 'FI', 5),
          ('Fiyi', 'República de las Islas Fiyi (Fiji)', 'FJ', 9),
          ('Francia', 'República Francesa', 'FR', 5),
          ('Gabón', 'República Gabonesa', 'GA', 8),
          ('Gambia', 'República de la Gambia', 'GM', 8),
          ('Georgia', 'Georgia', 'GE', 6),
          ('Ghana', 'República de Ghana', 'GH', 8),
          ('Gibraltar', 'Gibraltar', 'GI', 5),
          ('Granada', 'Granada', 'GD', 4),
          ('Grecia', 'República Helénica', 'GR', 5),
          ('Groenlandia', 'Groenlandia', 'GL', 1),
          ('Guam', 'Territorio de Guam', 'GU', 9),
          ('Guatemala', 'República de Guatemala', 'GT', 2),
          ('Guernsey', 'Bailiazgo de Guernsey', 'GF', 5),
          ('Guinea', 'República de Guinea', 'GN', 8),
          ('Guinea Ecuatorial', 'República de Guinea Ecuatorial', 'GQ', 8),
          ('Guinea-Bissau', 'República de Guinea-Bissau', 'GW', 8),
          ('Guyana', 'República Cooperativa de Guyana', 'GY', 3),
          ('Haití', 'República de Haití', 'HT', 4),
          ('Honduras', 'República de Honduras', 'HN', 2),
          ('Hong Kong', 'Región Administrativa Especial de Hong Kong', 'HK', 6),
          ('Hungría', 'República de Hungría', 'HU', 5),
          ('India', 'República de India', 'IN', 6),
          ('Indonesia', 'República de Indonesia', 'ID', 6),
          ('Irak', 'República de Irak', 'IQ', 6),
          ('Irán', 'República Islámica de Irán', 'IR', 6),
          ('Irlanda', 'República de Irlanda', 'IE', 5),
          ('Isla de Man', 'Isla de Man', 'IM', 5),
          ('Isla de Navidad', 'Territorio de la Isla de Navidad', 'CX', 6),
          ('Isla Norfolk', 'Territorio de las Islas Norfolk', 'NF', 9),
          ('Islandia', 'República de Islandia', 'IS', 5),
          ('Islas Caimán', 'Islas Caimán', 'KY', 2),
          ('Islas Cocos', 'Islas Cocos', 'CC', 6),
          ('Islas Cook', 'Islas Cook', 'CK', 9),
          ('Islas Feroe', 'Islas Feroe', 'FO', 5),
          ('Islas Malvinas', 'Islas Malvinas', 'FK', 10),
          ('Islas Marianas del Norte', 'Estado Libre Asociado de las Islas Marianas del Norte', 'MP', 9),
          ('Islas Marshall', 'República de las Islas Marshall', 'MH', 9),
          ('Islas Pitcairn', 'Islas Pitcairn', 'PN', 9),
          ('Islas Salomón', 'Islas Salomón', 'SB', 9),
          ('Islas Turcas y Caicos', 'Islas Turcas y Caicos', 'TC', 2),
          ('Islas Vírgenes Británicas', 'Islas Vírgenes Británicas', 'VG', 2),
          ('Islas Vírgenes de los Estados Unidos', 'Islas Vírgenes de los Estados Unidos', 'VI', 2),
          ('Israel', 'Estado de Israel', 'IL', 6),
          ('Italia', 'República Italiana', 'IT', 5),
          ('Jamaica', 'Jamaica', 'JM', 4),
          ('Japón', 'Japón', 'JP', 6),
          ('Jersey', 'Bailiazgo de Jersey', 'JE', 5),
          ('Jordania', 'Reino Hachemita de Jordania', 'JO', 6),
          ('Kazajistán', 'República de Kazajistán', 'KZ', 6),
          ('Kenia', 'República de Kenia', 'KE', 8),
          ('Kirguistán', 'República Kirguiza', 'KG', 6),
          ('Kiribati', 'República de Kiribati', 'KI', 9),
          ('Kosovo', 'República de Kosovo', 'XK', 5),
          ('Kuwait', 'Estado de Kuwait', 'KW', 6),
          ('Laos', 'República Democrática Popular Lao', 'LA', 6),
          ('Lesoto', 'Reino de Lesoto', 'LS', 8),
          ('Letonia', 'República de Letonia', 'LV', 5),
          ('Líbano', 'República del Líbano', 'LB', 6),
          ('Liberia', 'República de Liberia', 'LR', 8),
          ('Libia', 'República de Libia', 'LY', 8),
          ('Liechtenstein', 'Principado de Liechtenstein', 'LI', 5),
          ('Lituania', 'República de Lituania', 'LT', 5),
          ('Luxemburgo', 'Gran Ducado de Luxemburgo', 'LU', 5),
          ('Macao', 'Región Administrativa Especial de Macao', 'MO', 6),
          ('Macedonia', 'República de Macedonia3', 'MK', 5),
          ('Madagascar', 'República de Madagascar', 'MG', 8),
          ('Malasia', 'Federación de Malasia', 'MY', 6),
          ('Malaui', 'República de Malaui', 'MW', 8),
          ('Maldivas', 'República de las Maldivas', 'MV', 6),
          ('Malí', 'República de Malí', 'ML', 8),
          ('Malta', 'República de Malta', 'MT', 5),
          ('Marruecos', 'Reino de Marruecos', 'MA', 8),
          ('Mauricio', 'República de Mauricio', 'MU', 8),
          ('Mauritania', 'República Islámica de Mauritania', 'MR', 8),
          ('Micronesia', 'Estados Federados de Micronesia', 'FM', 9),
          ('Moldavia', 'República de Moldavia', 'MD', 5),
          ('Mónaco', 'Principado de Mónaco', 'MC', 5),
          ('Mongolia', 'Mongolia', 'MN', 6),
          ('Montenegro', 'República de Montenegro', 'ME', 5),
          ('Montserrat', 'Montserrat', 'MS', 2),
          ('Mozambique', 'República de Mozambique', 'MZ', 8),
          ('Nagorno Karabaj', 'República de Nagorno Karabaj', 'XA', 7),
          ('Namibia', 'República de Namibia', 'NA', 8),
          ('Nauru', 'República de Nauru', 'NR', 9),
          ('Nepal', 'República Federal Democrática de Nepal', 'NP', 6),
          ('Nicaragua', 'República de Nicaragua', 'NI', 2),
          ('Níger', 'República del Níger', 'NE', 8),
          ('Nigeria', 'República Federal de Nigeria', 'NG', 8),
          ('Niue', 'Niue', 'NU', 9),
          ('Noruega', 'Reino de Noruega', 'NO', 5),
          ('Nueva Caledonia', 'Territorio de Nueva Caledonia y dependencias', 'NC', 9),
          ('Nueva Zelanda', 'Nueva Zelanda', 'NZ', 9),
          ('Omán', 'Sultanato de Omán', 'OM', 6),
          ('Osetia del Sur', 'República de Osetia del Sur', 'XB', 7),
          ('Países Bajos / Holanda', 'Reino de los Países Bajos', 'NL', 5),
          ('Pakistán', 'República Islámica de Pakistán', 'PK', 6),
          ('Palaos', 'República de Palaos', 'PW', 9),
          ('Palestina', 'Autoridad Palestina de Cisjordania y la Franja de Gaza', 'PS', 6),
          ('Panamá', 'República de Panamá', 'PA', 2),
          ('Papúa Nueva Guinea', 'Estado Independiente de Papúa Nueva Guinea', 'PG', 9),
          ('Paraguay', 'República del Paraguay', 'PY', 3),
          ('Perú', 'República del Perú', 'PE', 3),
          ('Polinesia Francesa', 'Polinesia Francesa', 'PF', 9),
          ('Polonia', 'República de Polonia', 'PL', 5),
          ('Portugal', 'República Portuguesa', 'PT', 5),
          ('Puerto Rico', 'Estado Libre Asociado de Puerto Rico', 'PR', 4),
          ('Reino Unido', 'Reino Unido de Gran Bretaña e Irlanda del Norte', 'GB', 5),
          ('Republica Centroafricana', 'República Centroafricana', 'CF', 8),
          ('Republica Checa', 'República Checa', 'CZ', 5),
          ('Republica del Congo', 'República del Congo', 'CG', 8),
          ('Republica del Norte de Chipre', 'República Turca del Norte de Chipre', 'XC', 5),
          ('Republica Democratica del Congo', 'República Democrática del Congo', 'CD', 8),
          ('República Dominicana', 'República Dominicana', 'DO', 4),
          ('Ruanda', 'República de Ruanda', 'RW', 8),
          ('Rumania', 'Rumania', 'RO', 5),
          ('Rusia', 'Federación Rusa', 'RU', 7),
          ('Sahara Occidental', 'República Árabe Saharaui Democrática', 'EH', 8),
          ('Samoa', 'Estado Independiente de Samoa', 'WS', 9),
          ('Samoa Americana', 'Territorio de la Samoa Americana', 'AS', 9),
          ('San Bartolomé', 'San Bartolomé', 'BL', 2),
          ('San Cristóbal y Nieves', 'Federación de San Cristóbal y Nieves', 'KN', 4),
          ('San Marino', 'Serenísima República de San Marino', 'SM', 5),
          ('San Martín (Francia)', 'San Martín', 'MF', 2),
          ('San Martín (Países Bajos)', 'Sint Maarten', 'SX', 2),
          ('San Pedro y Miquelón', 'San Pedro y Miquelón', 'PM', 1),
          ('San Vicente y las Granadinas', 'San Vicente y las Granadinas', 'VC', 4),
          ('Santa Elena, Ascensión y Tristán de Acuña', 'Santa Elena, Ascensión y Tristán de Acuña', 'SH', 10),
          ('Santa Lucía', 'Santa Lucía', 'LC', 4),
          ('Santo Tomé y Príncipe', 'República Democrática de Santo Tomé y Príncipe', 'ST', 8),
          ('Senegal', 'República de Senegal', 'SN', 8),
          ('Serbia', 'República de Serbia', 'RS', 5),
          ('Seychelles', 'República de Seychelles', 'SC', 8),
          ('Sierra Leona', 'República de Sierra Leona', 'SL', 8),
          ('Singapur', 'República de Singapur', 'SG', 6),
          ('Siria', 'República Árabe Siria', 'SY', 6),
          ('Somalia', 'Somalia', 'SO', 8),
          ('Somalilandia', 'República de Somalilandia', 'XD', 8),
          ('Sri Lanka', 'República Democrática Socialista de Sri Lanka', 'LK', 6),
          ('Suazilandia', 'Reino de Suazilandia', 'SZ', 8),
          ('Sudáfrica', 'República de Sudáfrica', 'ZA', 8),
          ('Sudán', 'República del Sudán', 'SD', 8),
          ('Sudán del Sur', 'República de Sudán del Sur', 'SS', 8),
          ('Suecia', 'Reino de Suecia', 'SE', 5),
          ('Suiza', 'Confederación Helvética', 'CH', 5),
          ('Surinam', 'República de Surinam', 'SR', 3),
          ('Svalbard', 'Svalbard y Jan Mayen', 'SJ', 5),
          ('Tailandia', 'Reino de Tailandia', 'TH', 6),
          ('Taiwán', 'República de China', 'TW', 6),
          ('Tanzania', 'República Unida de Tanzania', 'TZ', 8),
          ('Tayikistán', 'República de Tayikistán', 'TJ', 6),
          ('Timor Oriental', 'República Democrática de Timor Oriental', 'TL', 6),
          ('Togo', 'República Togolesa', 'TG', 8),
          ('Tokelau', 'Tokelau', 'TK', 9),
          ('Tonga', 'Reino de Tonga', 'TO', 9),
          ('Transnistria', 'República Moldava Pridnestroviana', 'XE', 5),
          ('Trinidad y Tobago', 'República de Trinidad y Tobago', 'TT', 4),
          ('Túnez', 'República Tunecina', 'TN', 8),
          ('Turkmenistán', 'República de Turkmenistán', 'TM', 6),
          ('Turquía', 'República de Turquía', 'TR', 7),
          ('Tuvalu', 'Tuvalu', 'TV', 9),
          ('Ucrania', 'Ucrania', 'UA', 5),
          ('Uganda', 'República de Uganda', 'UG', 8),
          ('Uruguay', 'República Oriental del Uruguay', 'UY', 3),
          ('Uzbekistán', 'República de Uzbekistán', 'UZ', 6),
          ('Vanuatu', 'República de Vanuatu', 'VU', 9),
          ('Venezuela', 'República Bolivariana de Venezuela', 'VE', 3),
          ('Vietnam', 'República Socialista de Vietnam', 'VN', 6),
          ('Wallis y Futuna', 'Islas Wallis y Futuna', 'WF', 9),
          ('Yemen', 'República del Yemen', 'YE', 6),
          ('Yibuti', 'República de Yibuti', 'DJ', 8),
          ('Zambia', 'República de Zambia', 'ZM', 8),
          ('Zimbabue', 'República de Zimbabue', 'ZW', 8))

for i in Paises:
    print(i)
    p = Pais(nombre=i[0], nombre_extendido=i[1], codigo=i[2], zona=ZonaPais(pk=i[3]))
    p.save()


Estados = (
    ('Aguascalientes', Pais.objects.get(pais='México').id),
    ('Baja California', Pais.objects.get(pais='México').id),
    ('Baja California Sur', Pais.objects.get(pais='México').id),
    ('Campeche', Pais.objects.get(pais='México').id),
    ('Chiapas', Pais.objects.get(pais='México').id),
    ('Chihuahua', Pais.objects.get(pais='México').id),
    ('Ciudad de México', Pais.objects.get(pais='México').id),
    ('Coahuila de Zaragoza', Pais.objects.get(pais='México').id),
    ('Colima', Pais.objects.get(pais='México').id),
    ('Durango', Pais.objects.get(pais='México').id),
    ('Guanajuato', Pais.objects.get(pais='México').id),
    ('Guerrero', Pais.objects.get(pais='México').id),
    ('Hidalgo', Pais.objects.get(pais='México').id),
    ('Jalisco', Pais.objects.get(pais='México').id),
    ('Estado de México', Pais.objects.get(pais='México').id),
    ('Michoacán de Ocampo', Pais.objects.get(pais='México').id), #16
    ('Morelos', Pais.objects.get(pais='México').id),
    ('Nayarit', Pais.objects.get(pais='México').id),
    ('Nuevo León', Pais.objects.get(pais='México').id),
    ('Oaxaca', Pais.objects.get(pais='México').id),
    ('Puebla', Pais.objects.get(pais='México').id),
    ('Querétaro de Arteaga', Pais.objects.get(pais='México').id),
    ('Quintana Roo', Pais.objects.get(pais='México').id),
    ('San Luis Potosí', Pais.objects.get(pais='México').id), # 24
    ('Sinaloa', Pais.objects.get(pais='México').id),
    ('Sonora', Pais.objects.get(pais='México').id),
    ('Tabasco', Pais.objects.get(pais='México').id),
    ('Tamaulipas', Pais.objects.get(pais='México').id),
    ('Tlaxcala', Pais.objects.get(pais='México').id),
    ('Veracruz de Ignacio de la Llave', Pais.objects.get(pais='México').id),
    ('Yucatán', Pais.objects.get(pais='México').id),
    ('Zacatecas', Pais.objects.get(pais='México').id),
    ('Bogotá', Pais.objects.get(pais='Colombia').id),
    ('Antioquia', Pais.objects.get(pais='Colombia').id),
    ('Bern', Pais.objects.get(pais='Suiza').id),
    ('Zúrich', Pais.objects.get(pais='Suiza').id),
    ('Provincia de León', Pais.objects.get(pais='España').id),
    ('Comunidad de Madrid', Pais.objects.get(pais='España').id),
    ('Alicante', Pais.objects.get(pais='España').id),
    ('Barcelona', Pais.objects.get(pais='España').id),
    ('Provincia de Macerata', Pais.objects.get(pais='Italia').id),
    ('Isla de Francia', Pais.objects.get(pais='Francia').id),
    ('El Cairo', Pais.objects.get(pais='Egipto').id),
    ('Santiago', Pais.objects.get(pais='Chile').id),
    ('Lima', Pais.objects.get(pais='Perú').id),
    ('Viena', Pais.objects.get(pais='Austria').id),
    ('Virginia', Pais.objects.get(pais='Estados Unidos de América').id),
    ('Texas', Pais.objects.get(pais='Estados Unidos de América').id),
    ('California', Pais.objects.get(pais='Estados Unidos de América').id),
    ('Massachusetts', Pais.objects.get(pais='Estados Unidos de América').id),
    ('Míchigan', Pais.objects.get(pais='Estados Unidos de América').id),
    ('Indiana', Pais.objects.get(pais='Estados Unidos de América').id),
    ('Nueva York', Pais.objects.get(pais='Estados Unidos de América').id),
    ('Wiltshire', Pais.objects.get(pais='Reino Unido').id),
    ('Inglaterra', Pais.objects.get(pais='Reino Unido').id),
    ('Caracas', Pais.objects.get(pais='Venezuela').id),
    ('Loreto', Pais.objects.get(pais='Perú').id),
    ('Leoncio Prado', Pais.objects.get(pais='Perú').id),
    ('Montevideo', Pais.objects.get(pais='Uruguay').id),
    ('Overijssel', Pais.objects.get(pais='Países Bajos / Holanda').id),
    ('Buenos Aires', Pais.objects.get(pais='Argentina').id),
    ('Queensland', Pais.objects.get(pais='Australia').id),
    ('Cochabamba', Pais.objects.get(pais='Bolivia').id),
    ('Baviera', Pais.objects.get(pais='Alemania').id)



)

for i in Estados:
    e = Estado(estado=i[0], pais=Pais(pk=i[1]))
    e.save()


Ciudades = (
    ('Morelia', Estado.objects.get(estado='Michoacán de Ocampo').id),
    ('Ciudad de México, CDMX', Estado.objects.get(estado='Ciudad de México').id),
    ('Texcoco de Mora', Estado.objects.get(estado='Estado de México').id),
    ('Naucalpan de Juárez', Estado.objects.get(estado='Estado de México').id),
    ('Guadalajara', Estado.objects.get(estado='Jalisco').id),
    ('Monterrey', Estado.objects.get(estado='Nuevo León').id),
    ('Bogotá D.C.', Estado.objects.get(estado='Bogotá').id),
    ('Bern', Estado.objects.get(estado='Bern').id),
    ('León ', Estado.objects.get(estado='Provincia de León').id),
    ('Madrid', Estado.objects.get(estado='Comunidad de Madrid').id),
    ('Recanati', Estado.objects.get(estado='Provincia de Macerata').id),
    ('León', Estado.objects.get(estado='Guanajuato').id),
    ('Tingambato ', Estado.objects.get(estado='Michoacán de Ocampo').id),
    ('París', Estado.objects.get(estado='Isla de Francia').id),
    ('Zamora', Estado.objects.get(estado='Michoacán de Ocampo').id),
    ('Uruapan', Estado.objects.get(estado='Michoacán de Ocampo').id),
    ('El Cairo', Estado.objects.get(estado='El Cairo').id),
    ('Ciudad Juárez', Estado.objects.get(estado='Chihuahua').id),
    ('San Luis Potosí', Estado.objects.get(estado='San Luis Potosí').id),
    ('Santiago', Estado.objects.get(estado='Santiago').id),
    ('Xalapa ', Estado.objects.get(estado='Veracruz de Ignacio de la Llave').id),
    ('Lima', Estado.objects.get(estado='Lima').id),
    ('Camerino', Estado.objects.get(estado='Provincia de Macerata').id),
    ('Viena', Estado.objects.get(estado='Viena').id),
    ('Washington, D.C.', Estado.objects.get(estado='Virginia').id),
    ('Arlington', Estado.objects.get(estado='Texas').id),
    ('Swindon', Estado.objects.get(estado='Wiltshire').id),
    ('Pichátaro', Estado.objects.get(estado='Michoacán de Ocampo').id),
    ('La Piedad de Cavadas', Estado.objects.get(estado='Michoacán de Ocampo').id),
    ('Caracas', Estado.objects.get(estado='Caracas').id),
    ('Londres', Estado.objects.get(estado='Inglaterra').id),
    ('Patzcuaro', Estado.objects.get(estado='Michoacán de Ocampo').id),
    ('Ciudad de Iquitos', Estado.objects.get(estado='Loreto').id),
    ('Tingo María', Estado.objects.get(estado='Leoncio Prado').id),
    ('Swindon', Estado.objects.get(estado='Inglaterra').id),
    ('Mérida', Estado.objects.get(estado='Yucatán').id),
    ('Ciudad Victoria', Estado.objects.get(estado='Tamaulipas').id),
    ('Montevideo', Estado.objects.get(estado='Montevideo').id),
    ('Mexicali', Estado.objects.get(estado='Baja California').id),
    ('Davis', Estado.objects.get(estado='California').id),
    ('Redlands', Estado.objects.get(estado='California').id),
    ('Medellín', Estado.objects.get(estado='Antioquia').id),
    ('Norfolk', Estado.objects.get(estado='Inglaterra').id),
    ('Enschede', Estado.objects.get(estado='Overijssel').id),
    ('Buenos Aires', Estado.objects.get(estado='Buenos Aires').id),
    ('Brisbane', Estado.objects.get(estado='Queensland').id),
    ('Bellaterra', Estado.objects.get(estado='Barcelona').id),
    ('Aguascalientes', Estado.objects.get(estado='Aguascalientes').id),
    ('Toluca', Estado.objects.get(estado='Aguascalientes').id),
    ('Wayland', Estado.objects.get(estado='Massachusetts').id),
    ('Norcross', Estado.objects.get(estado='Georgia').id),
    ('Tepic', Estado.objects.get(estado='Nayarit').id),
    ('Boston', Estado.objects.get(estado='Massachusetts').id),
    ('Bloomington', Estado.objects.get(estado='Indiana').id),
    ('Cochabamba', Estado.objects.get(estado='Cochabamba').id),
    ('Zúrich', Estado.objects.get(estado='Zúrich').id),
    ('Ann Arbor', Estado.objects.get(estado='Míchigan').id),
    ('Wurzburgo', Estado.objects.get(estado='Baviera').id),
    ('San Vicente del Raspeig', Estado.objects.get(estado='Alicante').id),
    ('Nueva York', Estado.objects.get(estado='Nueva York').id)

)

for i in Ciudades:
    c = Ciudad(ciudad=i[0], estado=Estado(pk=i[1]))
    c.save()
    print("Agregada la ciudad " + i[0] + "para el estado " + str(Estado.objects.get(pk=i[1]).estado))











Instituciones = (
('Universidad Nacional Autónoma de México (UNAM)', Pais.objects.get(pais='México').id,
    (
        ('Universidad Nacional Autónoma de México (UNAM)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Universidad Nacional Autónoma de México, Campus Morelia (UNAM Morelia)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Unidad Académica de Geografía, Morelia (UNAM Morelia)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Centro de Investigaciones en Geografía Ambiental (CIGA)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Dirección General de Cooperación e Internacionalización (DGECI)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Instituto de Investigaciones en Ecosistemas y Sustentabilidad (IIES)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Centro de Ciencias de la Atmósfera', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Unidad de Posgrados', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Facultad de Ciencias', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Escuela Nacional de Estudios Superiores, Unidad Morelia (ENES Morelia)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Escuela Nacional de Estudios Superiores, Unidad León (ENES León)', Ciudad.objects.filter(ciudad='León', estado=Estado.objects.get(estado='Guanajuato').id)[0].id),
        ('Instituto de Geografía', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Instituto de Geología', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Instituto de Geofísica', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Instituto de Geofísica, Unidad Morelia (UNAM Morelia)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Centro de Ciencias de la Atmósfera', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Consejo Académico de Área en Ciencias Sociales (CAACS)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Facultad de Filosofía y Letras', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Facultad de Arquitectura', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Facultad de Filosofia y letras ', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Programa de Apoyo a Proyectos de Investigación e Innovación Tecnológica (PAPIIT)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Dirección General Asuntos del Personal Académico (DGAPA)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Posgrado en Geografia', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Laboratorio de Edafología "Nicolás Aguilera', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Dirección General de Bibiotecas (DGB)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id)
    )
 ),

('Universidad Michoacana de San Nicolás de Hidalgo (UMSNH)', Pais.objects.get(pais='México').id,
    (
        ('Instituto de Investigaciones Económicas y Empresariales (ININEE)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Coordinación de la Investigación Científica (CIC)', Ciudad.objects.get(ciudad='Morelia').id)
    )
 ),

('Universidad de Camerino', Pais.objects.get(pais='Italia').id,
    (
        ('Departamento de Geobotánica', Ciudad.objects.get(ciudad='Camerino').id),
        ('Braun Blanquetia', Ciudad.objects.get(ciudad='Camerino').id)
    )
 ),

('Universidad Nacional de Colombia', Pais.objects.get(pais='Colombia').id,
    (
        ('Instituto de Ciencias Naturales', Ciudad.objects.get(ciudad='Bogotá D.C.').id),
        ('Caldasia', Ciudad.objects.get(ciudad='Bogotá D.C.').id)
    )
 ),

('Universidad Intercultural Indígena de Michoacán (UIIM)', Pais.objects.get(pais='México').id,
    (
        ('UIIM Sede Pichátaro', Ciudad.objects.get(ciudad='Pichátaro').id),
        ('UIIM Unidad Académica Purépecha', Ciudad.objects.get(ciudad='Patzcuaro').id)
    )
 ),

('Universidad de León', Pais.objects.get(pais='España').id,
    (
        ('Universidad de León', Ciudad.objects.filter(ciudad='León', estado=Estado.objects.get(estado='Provincia de León').id)[0].id),
        ('', Ciudad.objects.filter(ciudad='León', estado=Estado.objects.get(estado='Provincia de León').id)[0].id)
    )
 ),

('University of Bern', Pais.objects.get(pais='Suiza').id, (('Mountain Research and Development', Ciudad.objects.get(ciudad='Bern').id))),

('Universidad Complutense de Madrid', Pais.objects.get(pais='España').id, (('Universidad Complutense de Madrid', Ciudad.objects.get(ciudad='Madrid').id))),

('Consejo Nacional de Ciencia y Tecnología (CONACYT)', Pais.objects.get(pais='México').id,
    (
        ('Consejo Nacional de Ciencia y Tecnología (CONACYT)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Fomento Regional para el Desarrollo Científico, Tecnológico y de Innovación (FORDECYT)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Innovate UK - CONACYT', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id)
    )
 ),

('Gobierno de la República Mexicana', Pais.objects.get(pais='México').id,
    (
        ('Secretaría de Desarrollo Social (SEDESOL)', Ciudad.objects.get(ciudad='').id)
    )
 ),

('Gobierno del Estado de Michoacán de Ocampo', Pais.objects.get(pais='México').id,
    (
        ('Secretaría de Innovación, Ciencia y Desarrollo Tecnológico (SICDET)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Consejo Estatal de Ciencia y Tecnología (CECTI)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Centro Estatal para el Desarrollo Municipal (CEDEMUN)', Ciudad.objects.get(ciudad='Morelia').id),
        ('Secretaría de Urbanismo y Medio Ambiente', Ciudad.objects.get(ciudad='Morelia').id),
        ('Centro Estatal de Tecnologías de Información y Comunicaciones (CETIC)', Ciudad.objects.get(ciudad='Morelia').id)
    )
 ),

('Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura (UNESCO)', Pais.objects.get(pais='Francia').id, (('Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura (UNESCO)', Ciudad.objects.get(ciudad='París').id))),

('El Colegio de Michoacán, A.C. (COLMICH)', Pais.objects.get(pais='México').id, (('El Colegio de Michoacán, A.C. (COLMICH)', Ciudad.objects.get(ciudad='La Piedad de Cavadas').id))),

('Interciencia, Revista de Ciencia y Tecnología de América Latina', Pais.objects.get(pais='Venezuela').id, (('Interciencia, Revista de Ciencia y Tecnología de América Latina', Ciudad.objects.get(ciudad='Caracas').id))),

('Hindawi Publishing Corporation', Pais.objects.get(pais='Reino Unido').id, (('Advances in Meteorology', Ciudad.objects.get(ciudad='Londres').id))),

('Universidad Autónoma de Ciudad Juárez', Pais.objects.get(pais='México').id,
    (
        ('Instituto de Arquitectura, Diseño y Arte', Ciudad.objects.get(ciudad='Ciudad Juárez').id),
        ('Departamento. de Arquitectura', Ciudad.objects.get(ciudad='Ciudad Juárez').id),
        ('Programa Académico de Geoinformática', Ciudad.objects.get(ciudad='Ciudad Juárez').id)
    )
 ),

('Universidad Valladolid', Pais.objects.get(pais='México').id, (('Instituto Valladolid Preparatoria', Ciudad.objects.get(ciudad='Morelia').id))),

('Instituto Tecnológico de Morelia', Pais.objects.get(pais='México').id, (('Instituto Tecnológico de Morelia', Ciudad.objects.get(ciudad='Morelia').id))),

('Universidad Autónoma de San Luis Potosí', Pais.objects.get(pais='México').id, (('Universidad Autónoma de San Luis Potosí', Ciudad.objects.get(ciudad='San Luis Potosí').id))),

('Pontificia Universidad Católica de Chile', Pais.objects.get(pais='Chile').id,
    (
        ('Pontificia Universidad Católica de Chile', Ciudad.objects.get(ciudad='Santiago').id),
        ('Comisión Nacional de Acreditación', Ciudad.objects.get(ciudad='Santiago').id)
    )
 ),

('Instituto de Ecología, A.C. (INECOL)', Pais.objects.get(pais='México').id, (('Instituto de Ecología, A.C. (INECOL)', Ciudad.objects.get(ciudad='Xalapa').id))),

('Red Mexicana de Cuencas Hidrográficas', Pais.objects.get(pais='México').id,  (('Red Mexicana de Cuencas Hidrográficas', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Universidad Agraria de la Selva', Pais.objects.get(pais='Perú').id, (('Revista Investigación y Amazonía', Ciudad.objects.get(ciudad='Tingo María').id))),

('Instituto de Investigaciones de la Amazonía Peruana', Pais.objects.get(pais='Perú').id, (('Instituto de Investigaciones de la Amazonía Peruana', Ciudad.objects.get(ciudad='Lima').id))),

('Asociación Española de Fitosociología (AEFA)', Pais.objects.get(pais='España').id,
    (
        ('Global Geobotany', Ciudad.objects.get(ciudad='Madrid').id),
        ('International Journal of Geobotanical Research', Ciudad.objects.get(ciudad='Madrid').id)
    )
 ),

('Austrian Development Cooperation (ADC)', Pais.objects.get(pais='Austria').id, (('APPEAR', Ciudad.objects.get(ciudad='Viena').id))),

('National Geographic Society (NGS)', Pais.objects.get(pais='Estados Unidos de América').id, (('National Geographic Society (NGS)', Ciudad.objects.get(ciudad='Washington, D.C.').id))),

('National Science Foundation (NSF)', Pais.objects.get(pais='Estados Unidos de América').id, (('National Science Foundation (NSF)', Ciudad.objects.get(ciudad='Arlington').id))),

('National Environmental Research Council (NERC)', Pais.objects.get(pais='Reino Unido').id, (('National Environmental Research Council (NERC)', Ciudad.objects.get(ciudad='Swindon').id))),

('Gobierno del Estado de Yucatán', Pais.objects.get(pais='México').id, (('Fondo Mixto Conacyt-Gobierno del Estado de Yucatán (FOMIX)', Ciudad.objects.get(ciudad='Mérida').id))),

('Universidad Autonoma de Tamaulipas', Pais.objects.get(pais='México').id, (('Universidad Autonoma de Tamaulipas', Ciudad.objects.get(ciudad='Ciudad Victoria').id))),

('Agencia Nacional de Investigación e Innovación de Uruguay (ANII)', 235, (('Fondo María Viñas', Ciudad.objects.get(ciudad='Montevideo').id))),

('Universidad Autónoma de Baja California', Pais.objects.get(pais='México').id, (('Universidad Autónoma de Baja California', Ciudad.objects.get(ciudad='Mexicali').id))),

('Universidad de California Davis', Pais.objects.get(pais='Estados Unidos de América').id, (('Universidad de California Davis', Ciudad.objects.get(ciudad='Davis').id))),

('Universidad de Antioquia', Pais.objects.get(pais='Colombia').id, (('Universidad de Antioquia', Ciudad.objects.get(ciudad='Medellín').id))),

('University of East Anglia', Pais.objects.get(pais='Reino Unido').id, (('University of East Anglia', Ciudad.objects.get(ciudad='Norfolk').id))),

('Universidad París 1 Panteón-Sorbona', Pais.objects.get(pais='Francia').id, (('Universidad París 1 Panteón-Sorbona', Ciudad.objects.get(ciudad='París').id))),

('Northwestern University', Pais.objects.get(pais='Estados Unidos de América').id, (('Northwestern University', Ciudad.objects.get(ciudad='').id))),

('University of Twente', Pais.objects.get(pais='Países Bajos / Holanda').id,
    (
        ('University of Twente', Ciudad.objects.get(ciudad='Enschede').id),
        ('International Institute for Geoinformation Sciences and Earth Observation', Ciudad.objects.get(ciudad='Enschede').id),
        ('Faculty of Geo-Information Science and Earth Observation', Ciudad.objects.get(ciudad='Enschede').id)
    )
 ),

('Universidad Autónoma de Madrid', Pais.objects.get(pais='España').id, (('Universidad Autónoma de Madrid', Ciudad.objects.get(ciudad='Madrid').id))),

('Universidad de Buenos Aires', Pais.objects.get(pais='Argentina').id, (('Universidad de Buenos Aires', Ciudad.objects.get(ciudad='Buenos Aires').id))),

('University of Queensland', Pais.objects.get(pais='Australia').id, (('University of Queensland', Ciudad.objects.get(ciudad='Brisbane').id))),

('Universidad Autónoma de Barcelona (UAB)', Pais.objects.get(pais='España').id, (('Universidad Autónoma de Barcelona (UAB)', Ciudad.objects.get(ciudad='Bellaterra').id))),

('El Colegio de México, A.C.', Pais.objects.get(pais='México').id, (('El Colegio de México, A.C.', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('LEAD International', Pais.objects.get(pais='México').id, (('LEAD International', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),


('Instituto Nacional de Estadística y Geografía (INEGI)', Pais.objects.get(pais='México').id, (('Instituto Nacional de Estadística y Geografía (INEGI)', Ciudad.objects.get(ciudad='Aguascalientes').id))),

('Sociedad Latinoamericana de Percepción Remota y Sistemas de Información Espacial (SELPER México)', Pais.objects.get(pais='México').id, (('Sociedad Latinoamericana de Percepción Remota y Sistemas de Información Espacial (SELPER México)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Universidad Autónoma del Estado de México (UAEMex)', Pais.objects.get(pais='México').id, (('Universidad Autónoma del Estado de México (UAEMex)', Ciudad.objects.get(ciudad='Toluca').id))),

('Open Geospatial Consortium (OGC)', Pais.objects.get(pais='Estados Unidos de América').id, (('Open Geospatial Consortium (OGC)', Ciudad.objects.get(ciudad='Wayland').id))),

('Gtt Imaging, S.A. de C.V.', Pais.objects.get(pais='México').id, (('Gtt Imaging, S.A. de C.V.', Ciudad.objects.get(ciudad='Guadalajara').id))),

('Instituto Nacional para el Federalismo y el Desarrollo Municipal (INAFED)', Pais.objects.get(pais='México').id, (('Instituto Nacional para el Federalismo y el Desarrollo Municipal (INAFED)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Secretaría de Medio Ambiente y Recursos Naturales (SEMARNAT)', Pais.objects.get(pais='México').id,
    (
        ('Secretaría de Medio Ambiente y Recursos Naturales (SEMARNAT)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Instituto Nacional de Ecología y Cambio Climático (INECC)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id)
    )
 ),

('International Institute for Geo-Information Science and Earth Observation', Pais.objects.get(pais='Países Bajos / Holanda').id, (('International Institute for Geo-Information Science and Earth Observation', Ciudad.objects.get(ciudad='Enschede').id))),

('Universidad Iberoamericana (UIA)', Pais.objects.get(pais='México').id,
    (
        ('Ibero OnLine', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id)
    )
 ),

('Centro de Capacitación en Calidad Sanitaria S.A. DE C.V.', Pais.objects.get(pais='México').id, (('Centro de Capacitación en Calidad Sanitaria S.A. DE C.V.', Ciudad.objects.get(ciudad='Monterrey').id))),

('Instituto Nacional de Antropología e Historia (INAH)', Pais.objects.get(pais='México').id,
    (
        ('Centro de Investigaciones y Estudios Superiores en Antropología Social (CIESAS)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Coordinación de Antropología', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id)
    )
 ),

('Universidad Autónoma Chapingo', Pais.objects.get(pais='México').id, (('Universidad Autónoma Chapingo', Ciudad.objects.get(ciudad='Texcoco de Mora').id))),

('Sistema de la Integración Centroamericana (SICA)', Pais.objects.get(pais='México').id, (('Comisión Centroamericana de Ambiente y Desarrollo (CCAD)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('National Aeronautics and Space Administration (NASA)', Pais.objects.get(pais='Estados Unidos de América').id, (('National Aeronautics and Space Administration (NASA)', Ciudad.objects.get(ciudad='Washington, D.C.').id))),

('Organización de las Naciones Unidas (ONU)', Pais.objects.get(pais='Estados Unidos de América').id, (('Banco Mundial (The World Bank)', Ciudad.objects.get(ciudad='Washington, D.C.').id))),

('Environmental Systems Research Institute (ESRI)', Pais.objects.get(pais='Estados Unidos de América').id, (('Environmental Systems Research Institute (ESRI)', Ciudad.objects.get(ciudad='Redlands').id))),

('Hexagon Geospatial', Pais.objects.get(pais='Estados Unidos de América').id, (('ERDAS Imagine', Ciudad.objects.get(ciudad='Norcross').id))),

('Sistemas de Información Geográfica, S.A. de C.V.', Pais.objects.get(pais='México').id, (('Sistemas de Información Geográfica, S.A. de C.V.', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Centro de Información y Comunicación Ambiental de Norte América, A.C. (CICEANA)', Pais.objects.get(pais='México').id, (('Centro de Información y Comunicación Ambiental de Norte América, A.C. (CICEANA)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Sociedad Mexicana de Geografía y Estadística, A.C.', Pais.objects.get(pais='México').id, (('Sociedad Mexicana de Geografía y Estadística, A.C.', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Dirección General de Geografía y Medio Ambiente', Pais.objects.get(pais='México').id, (('Dirección General de Geografía y Medio Ambiente', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Universidad Autónoma de Nayarit', Pais.objects.get(pais='México').id, (('Universidad Autónoma de Nayarit', Ciudad.objects.get(ciudad='Tepic').id))),

('El Colegio de Jalisco A.C.', Pais.objects.get(pais='México').id, (('El Colegio de Jalisco A.C.', Ciudad.objects.get(ciudad='Guadalajara').id))),

('Fundación Premio Nacional de Tecnología A.C.', Pais.objects.get(pais='México').id, (('Fundación Premio Nacional de Tecnología A.C.', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Universidad de Harvard', Pais.objects.get(pais='Estados Unidos de América').id,
    (
        ('Harvard Business Publishing', Ciudad.objects.get(ciudad='Boston').id)
    )
 ),

('Instituto Mexicano de la Propiedad Industrial (IMPI)', Pais.objects.get(pais='México').id, (('Instituto Mexicano de la Propiedad Industrial (IMPI)', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id))),

('Universidad Tecmilenio', Pais.objects.get(pais='México').id,
    (
        ('Universidad Tecmilenio', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id),
        ('Buzan Latin America', Ciudad.objects.get(ciudad='Ciudad de México, CDMX').id)
    )
 ),

('La Universidad de Indiana Bloomington', Pais.objects.get(pais='Estados Unidos de América').id,
    (
        ('Department of Political Science and Workshop in Political Theory and Policy Analysis', Ciudad.objects.get(ciudad='Bloomington').id),
        ('Workshop in Political Theory and Policy Analysis', Ciudad.objects.get(ciudad='Bloomington').id),
        ('Vincent and Elinor Ostrom Workshop in Political Theory and Policy Analysis', Ciudad.objects.get(ciudad='Bloomington').id)
    )
 ),

('Universidad Mayor se San Simón', Pais.objects.get(pais='Bolivia').id, (('Centro de Levantamientos Aeroespaciales y Aplicaciones SIG para el Desarrollo Sostenible de los Recursos Naturales (CLAS)', Ciudad.objects.get(ciudad='Cochabamba').id))),

('Escuela Politécnica Federal de Zúrich (ETHZ)', Pais.objects.get(pais='Suiza').id, (('Institute of Hydromechanics and Water Management', Ciudad.objects.get(ciudad='Zúrich').id))),

('Universidad de Míchigan', Pais.objects.get(pais='Estados Unidos de América').id, (('Universidad de Míchigan', Ciudad.objects.get(ciudad='Ann Arbor').id))),

('ASPEL', Pais.objects.get(pais='México').id, (('ASPEL', Ciudad.objects.get(ciudad='Guadalajara').id))),

('Técnica Aplicada Internacional S.A. de C.V.', Pais.objects.get(pais='México').id, (('Técnica Aplicada Internacional S.A. de C.V.', Ciudad.objects.get(ciudad='Naucalpan de Juárez').id))),

('Universidad de Wurzburgo', Pais.objects.get(pais='Alemania').id, (('Universidad de Wurzburgo', Ciudad.objects.get(ciudad='Wurzburgo').id))),

('The Big Van Theory: científicos sobre ruedas', Pais.objects.get(pais='España').id, (('The Big Van Theory: científicos sobre ruedas', Ciudad.objects.get(ciudad='Madrid').id))),

('Universidad Complutense Madrid', Pais.objects.get(pais='España').id, (('Universidad Complutense Madrid', Ciudad.objects.get(ciudad='Madrid').id))),

('Escuela de Organización Industrial', Pais.objects.get(pais='España').id, (('Escuela de Organización Industrial', Ciudad.objects.get(ciudad='Madrid').id))),

('Gobierno de España', Pais.objects.get(pais='España').id, (('Gobierno de España', Ciudad.objects.get(ciudad='Madrid').id))),

('Universidad de Alicante', Pais.objects.get(pais='España').id, (('Instituto de Economía Internacional', Ciudad.objects.get(ciudad='San Vicente del Raspeig').id))),

('Interactive Advertising Bureau (IAB)', Pais.objects.get(pais='Estados Unidos de América').id, (('Interactive Advertising Bureau (IAB)', Ciudad.objects.get(ciudad='Nueva York').id))),

('Universidad Don Vasco', Pais.objects.get(pais='México').id, (('Universidad Don Vasco', Ciudad.objects.get(ciudad='Uruapan ').id))),


('Arkinet, S.A. De C.V.', Pais.objects.get(pais='México').id, (('Centro de capacitación de alto rendimiento', Ciudad.objects.get(ciudad='Morelia').id))),

('Corporación Universitaria para el Desarrollo de Internet, A.C. (CUDI)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Politécnica de Madrid', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Academia Mexicana de Impacto Ambiental', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Advanced Analytical Systems, S.A. de C.V.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Estatal de Sonora', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Banco Interamericano de Desarrollo (BID)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Sociedad Mexicana para la Divulgación de la Ciencia y la Técnica A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Centro de Investigación en Matemáticas', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Nacional de Tucumán', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Guadalajara', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Cádiz', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de La Habana', 56, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Paul Sabatier', Pais.objects.get(pais='Francia').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Politécnica de Valencia', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),

('International Social Science Council (ISSC)', Pais.objects.get(pais='Francia').id, ((''))),
('Instituo Nacional Electoral (INE)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de París I Panthéon-Sorbonne', Pais.objects.get(pais='Francia').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Politécnica de Cataluña', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Lérida', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Brístol', Pais.objects.get(pais='Reino Unido').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Nacional de Córdoba', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Sinkiang', 46, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Sonora', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autónoma de Baja California Sur (UABCS)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Academia de Ciencias de Cuba', 56, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Interamericana para el Desarrollo (UNID)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autonoma de Queretaro', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Northwestern', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Tecnológico y de Estudios Superiores de Monterrey (ITESM)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Queensland', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autónoma de Barcelona', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Wagenningen', Pais.objects.get(pais='Países Bajos / Holanda').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Hokkaido', 118, (('', Ciudad.objects.get(ciudad='').id))),
('Biocenosis, A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Alternare, A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Comisión Nacional Para el Conocimiento y Uso de la Biodiversidad (CONABIO)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Comisión Nacional de Áreas Naturales Protegidas (CONANP)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('H. Ayuntamiento de Morelia', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Santiago de Compostela', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Secretaría de Relaciones Exteriores (SRE)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Gobierno del Estado de Michoacán', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Alianza México REDD+', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Agencia Nacional de Promoción Científica y Tecnológica', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Fundación Produce Michoacán A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Fundación Gonzalo Río Arronte I.A.P.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Inter-American Institute for Global Change Research', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Gobierno del Estado de Jalisco', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Unión Geográfica Internacional (UGI)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('International Union for Conservation of Nature (IUCN)', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Centre National de la Recherche Scientifique (CNRS)', 175, (('', Ciudad.objects.get(ciudad='').id))),
('Secretaría de Medio Ambiente y Desarrollo Territorial (SEMADET Jalisco)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Querétaro', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de British Columbia', 42, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Illinois en Urbana-Champaign', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autónoma de Campeche', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('El Colegio de la Frontera Sur Unidad San Cristóbal (ECOSUR)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Federal de Minas Gerais', 33, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Estatal de Feira de Santana', 33, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Toulouse', Pais.objects.get(pais='Francia').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Granada', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Centro de Investigación en Alimentación y Desarrollo, A.C. (CIAD)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Guanajuato', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Netherlands organization for Scientific Research, (WOTRO)', Pais.objects.get(pais='Países Bajos / Holanda').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Texas en Austin', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Reserva de la Biósfera Santuario Mariposa Monarca', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Global Water Watch (GWW)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Grupo Balsas para Estudio y Manejo de Ecosistemas, A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Municipal de Planeación Morelia (IMPLAN)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Colegio de Postgraduados (COLPOS)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autónoma de Chiapas', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Nacional de la Patagonia San Juan Bosco', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Centro de estudios Patagónicos', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Comisión Nacional del Agua (CONAGUA)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Comisión Nacional Forestal (CONAFOR)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Grupo Interdisciplinario de Tecnología Rural Apropiada, A.C. (GIRA)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('International Maize and Wheat Improvement Center (CIMMYT)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Diputación Provincial de Barcelona', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Murcia', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Proyecto Arqueológico Yocavil', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Cooperación Alemana al Desarrollo GIZ', Pais.objects.get(pais='Alemania').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Florida', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('WWF México', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Organización de las Naciones Unidas para la Alimentación y la Agricultura', 42, (('', Ciudad.objects.get(ciudad='').id))),
('Dirección General de Desarrollo Institucional y Promoción', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Dirección de Manejo Integral de Cuencas Hídricas', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Comision Nacional de Vivienda (CONAVI)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Toulouse-Jean Jaurès', Pais.objects.get(pais='Francia').id, (('', Ciudad.objects.get(ciudad='').id))),
('La Universidad de Texas A&M', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Montreal', 42, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Tulane', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Nacional de General Sarmiento', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Wageningen University and Research Centre', Pais.objects.get(pais='Países Bajos / Holanda').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Cabo Verde', 39, (('', Ciudad.objects.get(ciudad='').id))),
('Centro di Ricerca, Sviluppo e Studi Superiori in Sardegna (CRS4)', 116, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Estatal de Washington', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Ciencias de Vida de Noruega (NMBU)', 162, (('', Ciudad.objects.get(ciudad='').id))),
('Centro de Investigación y de Estudios Avanzados del Instituto Politécnico Nacional (CINVESTAV)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Politécnico Nacional (IPN)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Pablo de Olavide', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Consejo Superior de Investigaciones Científicas (CSIC)', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Gobierno de Cataluña (Generalitat de Catalunya)', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto del Conurbano (ICO)', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Católica de Honduras (UNICAH)', 91, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Nacional de Investigaciones Forestles, Agrícolas y Pecuarias (INIFAP)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Sociedad Científica Latinoamericana de Agroecología (SOCLA)', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Honorable Concejo Deliberante', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Asociación Etnobiológica Mexicana A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autónoma de Guerrero', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Academia Mexicana de Ciencias', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Tecnológico Superior de Huetamo', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Tecnológica de Morelia', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Pedagógica Nacional', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Tecnológico Superior de Tacámbaro', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Secretaría de Educación Pública (SEP)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Morelia (UDEM)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Tecnológico del Valle de Morelia', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autónoma Metropolitana (UAM)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Tecnológico Superior de Puruándiro (ITESP)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Benemérita Universidad Autónoma de Puebla (BUAP)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Internacional de Andalucía (UNIA)', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de los Llanos', Pais.objects.get(pais='Colombia').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Nacional de La Plata (UNLP)', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Nacional de Cuyo (UNCUYO)', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Facultad Latinoamericana de Ciencias Sociales (FLACSO)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autónoma del Estado de Morelos', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Secretaria de Educación en el Estado de Michoacán de Ocampo (SEE Michoacán)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Quintana Roo', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Tecnológica de Madrid', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Internacional Jefferson', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Federal de Espíritu Santo (UFES)', 33, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad del Miño', 177, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de San Carlos de Guatemala', 84, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Veracruzana (UV)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Pontificia Universidad Javeriana', Pais.objects.get(pais='Colombia').id, (('', Ciudad.objects.get(ciudad='').id))),
('Tecnológico Nacional de México (TecNM)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto Venezolano de Investigaciones Científicas (IVIC)', 238, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Virtual del Estado de Michoacán (UNIVIM)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Petróleos Mexicanos (PEMEX)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Consejo Nacional de Población (CONAPO)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto para el Desarrollo Sustentable en Mesoamérica, AC', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Instituto de Ecologia y Sistemática', 56, (('', Ciudad.objects.get(ciudad='').id))),
('Signos Diseño & Publicidad', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Dirección General de Educación Tecnológica Agropecuaria (DGTA)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Tecnologías y Servicios Agrarios, S.A (Tragsatec)', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Meneu Distribucion, S.A.', Pais.objects.get(pais='España').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad de Dar es-Salam', 221, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Autónoma de Tlaxcala', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('CDMedia Soluciones', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Secretaría de Planeación y Desarrollo (SEPLADE)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Harlen Administrativo SA de CV', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('CODINET SA DE CV', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('International Society for the Study of Religion, Nature and Culture (ISSRNC)', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Conference of Latin Americanist Geographers (CLAG)', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('H. Ayuntamiento de Morelos', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Telebachillerato Michoacán', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('TECIF', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Fideicomisos Instituidos en Relación con la Agrícultura (FIRA)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Commission for Environmental Cooperation', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Vasco de Quiroga (UVAQ)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Ministerio de Infraestructura (provincia de Buenos Aires)', Pais.objects.get(pais='Argentina').id, (('', Ciudad.objects.get(ciudad='').id))),
('Espacio Autónomo A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Fondo Monarca, A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Fondo Mexicano para la Conservación de la Naturaleza, A.C. (FMCN)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Center for Latin American Studies (CLAS)', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Secretaría de Comunicaciones y Transportes (SCT)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Secretaría de Gobernación (SEGOB)', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('EcoLogic Development Fund', Pais.objects.get(pais='Estados Unidos de América').id, (('', Ciudad.objects.get(ciudad='').id))),
('Ecotecnologías, A.C.', Pais.objects.get(pais='México').id, (('', Ciudad.objects.get(ciudad='').id))),
('Universidad Nacional Agraria La Molina (UNALM)', 174, (('', Ciudad.objects.get(ciudad='').id))),


)


for i in Instituciones:
    e = Institucion(institucion=i[0], pais=Pais(pk=i[1]))
    e.save()

    """
    for j in i[2]:
        f = Dependencia(dependencia=j[0], institucion=Institucion(pk=e.id), ciudad=Ciudad(pk=[1]))
    """

