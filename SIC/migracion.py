import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SIC.settings")
import django
django.setup()

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from autoslug import AutoSlugField
from nucleo.models import Tag, ZonaPais, Pais, Estado, Ciudad, Region, Ubicacion, Institucion, Dependencia, Departamento, \
    User, Programa, AreaConocimiento, AreaWOS, AreaEspecialidad, ImpactoSocial, Cargo, \
    FinanciamientoUNAM, FinanciamientoExterno, Metodologia, Beca, Tesis, ProgramaLicenciatura, \
    ProgramaMaestria, ProgramaDoctorado, ProgramaEspecializacion, TipoEvento, Evento, Proyecto

from apoyo_institucional.models import Actividad, Comision, Representacion, CargoAcademicoAdministrativo, \
    RepresentanteAnteOrganoColegiado, ComisionAcademica, ApoyoTecnico, ApoyoOtraActividad

from desarrollo_tecnologico.models import TipoDesarrollo, Licencia, DesarrolloTecnologico

from difusion_cientifica.models import MemoriaInExtenso, PrologoLibro, Resena, OrganizacionEventoAcademico, ParticipacionEventoAcademico











Zonas = ('América del Norte', 'América Central', 'América del Sur', 'Antillas', 'Europa', 'Asia', 'Europa-Asia', 'África', 'Oceanía', 'Oceano Atlántico')

for i in Zonas:
    print(i)
    z = ZonaPais(zona=i)
    z.save()


Paises = (('México', 'Estados Unidos Mexicanos', 'MX', 1), ('Abjasia', 'República de Abjasia', 'AB', 6),
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


Estados = ('Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Chiapas', 'Chihuahua', 'Ciudad de México', 'Coahuila de Zaragoza', 'Colima', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'Estado de México', 'Michoacán de Ocampo', 'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro de Arteaga', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz de Ignacio de la Llave', 'Yucatán', 'Zacatecas')

for i in Estados:
    e = Estado(estado=i, pais=Pais(pk=1))
    e.save()


# fa_especializacion

Instituciones = (
('Universidad Nacional Autónoma de México (UNAM)', 1),
('Universidad Michoacana de San Nicolás de Hidalgo (UMSNH)', 1),
('Universidad Nacional de Colombia', 49),
('University of Bern', 216),
('Universidad de León', 67),
('Universidad Complutense de Madrid', 67),
('Universidad de Camerino', 116),
('CONACYT', 1),
('Gobierno del Estado de Michoacán de Ocampo', 1),
('UNESCO', 74),
('El Colegio de Michoacán, A.C. (COLMICH)', 1),
('SEDESOL', 1),
('Universidad Autónoma de Ciudad Juárez', 1),
('Universidad Valladolid', 1),
('Instituto Tecnológico de Morelia', 1),
('Universidad Intercultural Indígena de Michoacán', 1),
('Universidad Autónoma de San Luis Potosí', 1),
('Universidad Autónoma de Ciudad Juárez', 1),
('Pontificia Universidad Católica de Chile', 45),
('APPEAR', 16),
('NGS National Geographic Society', 68),
('NSF National Science Foundation', 68),
('National Environmental Research Council (NERC)', 179),
('Universidad Autonoma de Tamaulipas', 1),
('Agencia Nacional de Investigación e Innovación de Uruguay (ANII)', 235),
('Universidad Autónoma de Baja California', 1),
('Instituto de Ecología, A.C., Xalapa', 1),
('Universidad de California Davis', 68),
('Universidad de Antioquia, Medellín', 49),
('University of East Anglia', 179),
('Universidad París 1 Panteón-Sorbona', 74),
('Northwestern University', 68),
('University of Twente', 167),
('Universidad Autónoma de Madrid', 67),
('Universidad de Buenos Aires', 13),
('INECOL', 1),
('University of Queensland', 16),
('Universidad Autónoma de Barcelona (UAB)', 67),
('Universidad Autónoma Chapingo', 1),
('El Colegio de México, A.C.', 1),
('LEAD International', 68),
('Instituto Nacional de Estadística y Geografía (INEGI)', 1),
('SELPER México', 1),
('Open Geospatial Consortium', 68),
('Universidad Autónoma del Estado de México', 1),
('Gtt Imaging, S.A. de C.V.', 1),
('Instituto Nacional para el Federalismo y el Desarrollo Municipal', 1),
('Instituto Nacional de Ecología', 1),
('International Institute for Geo-Information Science and Earth Observation', 167),
('Universidad Iberoamericana', 1),
('Instituo Nacional Electoral (INE)', 1),
('Centro de Capacitación en Calidad Sanitaria S.A. DE C.V.', 1),
('Comisión Centroamericana de Ambiente y Desarrollo (CCAD)', 1),
('National Aeronautics and Space Administration (NASA)', 68),
('Banco Mundial', 68),
('Sistemas de Información Geográfica, S.A. de C.V.', 1),
('Centro de Información y Comunicación Ambiental de Norte América, A.C. (CICEANA)', 1),
('Sociedad Mexicana de Geografía y Estadística, A.C.', 1),
('Universidad Autónoma de Nayarit', 1),
('El Colegio de Jalisco A.C.', 1),
('Universidad Autónoma de Nayarit', 1),
('Instituto Nacional de Antropología e Historia', 1),
('Fundación Premio Nacional de Tecnología A.C.', 1),
('Consejo Estatal de Ciencia y Tecnología del Estado de Michoacán (CECTI)', 1),
('Harvard Business Publishing', 68),
('Instituto Mexicano de la Propiedad Industrial (IMPI)', 1),
('Buzan Latin America', 1),
('Universidad Tecmilenio', 1),
('La Universidad de Indiana Bloomington', 68),
('Centro de Levantamientos Aeroespaciales y Aplicaciones SIG para el Desarrollo Sostenible de los Recursos Naturales (CLAS-ITC)', 30),
('International Institute for Geoinformation Sciences and Earth Observation (ITC)', 167)
('Institute of Hydromechanics and Water Management', 216),
('Faculty of Geo-Information Science and Earth Observation (ITC)', 167),
('Universidad de Michigan', 68),
('Universidad de Wurzburgo', 6),
('ASPEL', 1),
('Técnica Aplicada Internacional S.A. de C.V.', 1),
('Universidad Complutense Madrid', 67),
('Escuela de Organización Industrial', 67),
('Universidad de Alicante', 67),
('Interactive Advertising Bureau ', 68),
('Instituto Tecnológico de Morelia', 1),
('Universidad Don Vasco', 1),
('Centro Estatal de Tecnologías de Información y Comunicaciones (CETIC)', 1),
('Arkinet, S.A. De C.V.', 1),
('Corporación Universitaria para el Desarrollo de Internet, A.C. (CUDI)', 1),
('Universidad Politécnica de Madrid', ),
('Academia Mexicana de Impacto Ambiental', 1),
('Advanced Analytical Systems, S.A. de C.V.', 1),
('Universidad Estatal de Sonora', 1),
('Banco Interamericano de Desarrollo (BID)', 1),
('Sociedad Mexicana para la Divulgación de la Ciencia y la Técnica A.C.', 1),
('Centro de Investigación en Matemáticas', 1),
('Universidad Nacional de Tucumán', 13),
('Universidad de Guadalajara', 1),
('Universidad de Cádiz', 67),
('Universidad de La Habana', 56),
('Universidad Paul Sabatier', 74),
('Universidad Intercultural Pichátaro', 1),
('Universidad Politécnica de Valencia', 67),
('Universidad Autónoma Chapingo', 1),
('Universidad Mayor se San Simón', 30),
('Universidad Autónoma del Estado de México (UAEMEX)', 1),
('Universidad de París I Panthéon-Sorbonne', 74),
('Universidad Politécnica de Cataluña', 67),
('Universidad de Lérida', 67),
('Universidad de Brístol', 179),
('Universidad Autónoma de Madrid', 67),
('Universidad Nacional de Córdoba', 13),
('Instituto Nacional de Antropología e Historia', 1),
('Universidad de Sinkiang', 46),
('Universidad de Buenos Aires', 13),
('Universidad de Sonora', 1),
('Universidad Autónoma de Baja California', 1),
('Academia de Ciencias de Cuba', 56),
('Universidad Interamericana para el Desarrollo (UNID)', 1),
('Universidad Autonoma de Queretaro', 1),
('Universidad Northwestern', 68),
('Instituto Tecnológico y de Estudios Superiores de Monterrey (ITESM)', 1),
('Universidad de Queensland', 1),
('Universidad Autónoma de Barcelona', 67),
('Universidad de Wagenningen', 167),
('Universidad de Hokkaido', 118),
('Biocenosis A.C.', 1),
('Alternare A.C.', 1),
('Comisión Nacional Para el Conocimiento y Uso de la Biodiversidad (CONABIO)', 1),
('Comisión Nacional de Áreas Naturales Protegidas (CONANP)', 1),
('H. Ayuntamiento de Morelia', 1),
('Universidad de Santiago de Compostela', 67),
('Secretaría de Relaciones Exteriores (SRE)', 1),
('Gobierno del Estado de Michoacán', 1),
('Alianza México REDD+', 1),
('Agencia Nacional de Promoción Científica y Tecnológica', 13),
('Fundación Produce Michoacán A.C.', 1),
('Fundación Gonzalo Río Arronte I.A.P.', 1),
('Inter-American Institute for Global Change Research', 68),
('Secretaría de Medio Ambiente y Recursos Naturales (SEMARNAT)', 1),
('Gobierno del Estado de Jalisco', 1),
('Unión Geográfica Internacional (UGI)', 1),
('International Union for Conservation of Nature (IUCN)', 68),
('Centre National de la Recherche Scientifique (CNRS)', 175),
('Secretaría de Medio Ambiente y Desarrollo Territorial (SEMADET Jalisco)', 1),
('Universidad de Querétaro', 1),
('Universidad de British Columbia', 42),
('Universidad de Illinois en Urbana-Champaign', 68),
('Universidad Autónoma de Campeche', 1),
('El Colegio de la Frontera Sur Unidad San Cristóbal (ECOSUR)', 1),
('Universidad Federal de Minas Gerais', 33),
('Universidad Estatal de Feira de Santana', 33),
('Universidad de Toulouse', 74),
('Universidad de Granada', 67),
('Centro de Investigación en Alimentación y Desarrollo, A.C. (CIAD)', 1),
('Universidad de Guanajuato', 1),
('Netherlands organization for Scientific Research, (WOTRO)', 167),
('Universidad de Texas en Austin', 67),
('Reserva de la Biósfera Santuario Mariposa Monarca', 1),
('Global Water Watch (GWW)', 1),
('Grupo Balsas para Estudio y Manejo de Ecosistemas, A.C.', 1),
('Instituto Municipal de Planeación Morelia (IMPLAN)', 1),
('Agencia Nacional de Promoción Científica y Tecnológica', 13),
('Centro de Investigaciones y Estudios Superiores en Antropología Social (CIESAS)', 1),
('Colegio de Postgraduados (COLPOS)', 1),
('Universidad Autónoma de Chiapas', 1),
('Universidad Nacional de la Patagonia San Juan Bosco', 13),
('Centro de estudios Patagónicos', 13),
('Comisión Nacional del Agua (CONAGUA)', 1),
('Comisión Nacional Forestal (CONAFOR)', 1),
('Grupo Interdisciplinario de Tecnología Rural Apropiada, A.C. (GIRA)', 1),
('Diputación Provincial de Barcelona', 67),
('Universidad de Murcia', 67),
('Proyecto Arqueológico Yocavil', 13),
('Cooperación Alemana al Desarrollo GIZ', 6),
('Universidad de Florida', 68),
('WWF México', 1),
('Organización de las Naciones Unidas para la Alimentación y la Agricultura', 42),
('Dirección General de Desarrollo Institucional y Promoción', 1),
('Dirección de Manejo Integral de Cuencas Hídricas', 1),
('Instituto Nacional de Ecología y cambio Climático (INECC)', 1),
('Instituto Nacional de Antropología e Historia (INAH)', 1),
('Comision Nacional de Vivienda (CONAVI)', ),
('Universidad de Toulouse-Jean Jaurès', 74),
('La Universidad de Texas A&M', 68),
('Universidad de Montreal', 42),
('Universidad Tulane', 68),
('Universidad Nacional de General Sarmiento', 13),
('Wageningen University and Research Centre', 167),
('Universidad de Cabo Verde', 39),
('Centro di Ricerca, Sviluppo e Studi Superiori in Sardegna (CRS4)', 116),
('Universidad Estatal de Washington', 68),
('Universidad de Ciencias de Vida de Noruega (NMBU)', 162),
('Centro de Investigación y de Estudios Avanzados del Instituto Politécnico Nacional (CINVESTAV)', 1),
('Instituto Politécnico Nacional (IPN)', 1),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),
('', ),

)
