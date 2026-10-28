import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

metro_cdmx = {
    "Línea 1": [
        "Pantitlán", "Zaragoza", "Gómez Farías", "Boulevard Puerto Aéreo",
        "Balbuena", "Moctezuma", "San Lázaro", "Candelaria", "Merced",
        "Pino Suárez", "Isabel la Católica", "Salto del Agua", "Balderas",
        "Cuauhtémoc", "Insurgentes", "Sevilla", "Chapultepec", "Juanacatlán",
        "Tacubaya", "Observatorio"
    ],
    "Línea 2": [
        "Cuatro Caminos", "Panteones", "Tacuba", "Cuitláhuac", "Popotla",
        "Colegio Militar", "Normal", "San Cosme", "Revolución", "Hidalgo",
        "Bellas Artes", "Allende", "Zócalo/Tenochtitlan", "Pino Suárez",
        "San Antonio Abad", "Chabacano", "Viaducto", "Xola", "Villa de Cortés",
        "Nativitas", "Portales", "Ermita", "General Anaya", "Tasqueña"
    ],
    "Línea 3": [
        "Indios Verdes", "Deportivo 18 de Marzo", "Potrero", "La Raza",
        "Tlatelolco", "Guerrero", "Hidalgo", "Juárez", "Balderas",
        "Niños Héroes", "Hospital General", "Centro Médico",
        "Etiopía/Plaza de la Transparencia", "Eugenia", "División del Norte",
        "Zapata", "Coyoacán", "Viveros/Derechos Humanos",
        "Miguel Ángel de Quevedo", "Copilco", "Universidad"
    ],
    "Línea 4": [
        "Martín Carrera", "Talismán", "Bondojito", "Consulado",
        "Canal del Norte", "Morelos", "Candelaria", "Fray Servando",
        "Jamaica", "Santa Anita"
    ],
    "Línea 5": [
        "Pantitlán", "Hangares", "Terminal Aérea", "Oceanía", "Aragón",
        "Eduardo Molina", "Consulado", "Valle Gómez", "Misterios", "La Raza",
        "Autobuses del Norte", "Instituto del Petróleo", "Politécnico"
    ],
    "Línea 6": [
        "El Rosario", "Tezozómoc", "UAM-Azcapotzalco",
        "Ferrería/Arena Ciudad de México", "Norte 45", "Vallejo",
        "Instituto del Petróleo", "Lindavista", "Deportivo 18 de Marzo",
        "La Villa-Basílica", "Martín Carrera"
    ],
    "Línea 7": [
        "El Rosario", "Aquiles Serdán", "Camarones", "Refinería", "Tacuba",
        "San Joaquín", "Polanco", "Auditorio", "Constituyentes", "Tacubaya",
        "San Pedro de los Pinos", "San Antonio", "Mixcoac",
        "Barranca del Muerto"
    ],
    "Línea 8": [
        "Garibaldi/Lagunilla", "Bellas Artes", "San Juan de Letrán",
        "Salto del Agua", "Doctores", "Obrera", "Chabacano", "La Viga",
        "Santa Anita", "Coyuya", "Iztacalco", "Apatlaco", "Aculco",
        "Escuadrón 201", "Atlalilco", "Iztapalapa", "Cerro de la Estrella",
        "UAM-I", "Constitución de 1917"
    ],
    "Línea 9": [
        "Tacubaya", "Patriotismo", "Chilpancingo", "Centro Médico",
        "Lázaro Cárdenas", "Chabacano", "Jamaica", "Mixiuhca", "Velódromo",
        "Ciudad Deportiva", "Puebla", "Pantitlán"
    ],
    "Línea A": [
        "Pantitlán", "Agrícola Oriental", "Canal de San Juan", "Tepalcates",
        "Guelatao", "Peñón Viejo", "Acatitla", "Santa Marta", "Los Reyes",
        "La Paz"
    ],
    "Línea B": [
        "Buenavista", "Guerrero", "Garibaldi/Lagunilla", "Lagunilla", "Tepito",
        "Morelos", "San Lázaro", "Ricardo Flores Magón", "Romero Rubio",
        "Oceanía", "Deportivo Oceanía", "Bosque de Aragón", "Villa de Aragón",
        "Nezahualcóyotl", "Impulsora", "Río de los Remedios", "Múzquiz",
        "Ecatepec", "Olímpica", "Plaza Aragón", "Ciudad Azteca"
    ],
    "Línea 12": [
        "Mixcoac", "Insurgentes Sur", "Hospital 20 de Noviembre", "Zapata",
        "Parque de los Venados", "Eje Central", "Ermita", "Mexicaltzingo",
        "Atlalilco", "Culhuacán", "San Andrés Tomatlán", "Lomas Estrella",
        "Calle 11", "Periférico Oriente", "Tezonco", "Olivos", "Nopalera",
        "Zapotitlán", "Tlaltenco", "Tláhuac"
    ]
}

for linea, estaciones in metro_cdmx.items():
    nx.add_path(G, estaciones, linea=linea)

plt.figure(figsize=(24, 20))

pos = {
    # ================= LINEA 1 (ROSA) =================
    "Observatorio": (-16, 0),
    "Tacubaya": (-13, 0),
    "Juanacatlán": (-11, 0),
    "Chapultepec": (-9, 0),
    "Sevilla": (-7, 0),
    "Insurgentes": (-5, 0),
    "Cuauhtémoc": (-3, 0),
    "Balderas": (-1, 0),
    "Salto del Agua": (1, 0),
    "Isabel la Católica": (3, 0),
    "Pino Suárez": (5, 0),
    "Merced": (7, 0),
    "Candelaria": (9, 0),
    "San Lázaro": (11, 0),
    "Moctezuma": (13, 0),
    "Balbuena": (15, 0),
    "Boulevard Puerto Aéreo": (17, 0),
    "Gómez Farías": (19, 0),
    "Zaragoza": (21, 0),
    "Pantitlán": (24, 0),

    # ================= LINEA 2 (AZUL) =================
    "Cuatro Caminos": (-11, 14),
    "Panteones": (-11, 12),
    "Tacuba": (-11, 10),
    "Cuitláhuac": (-9, 8),
    "Popotla": (-7, 7),
    "Colegio Militar": (-5, 6),
    "Normal": (-4, 5),
    "San Cosme": (-3, 4),
    "Revolución": (-2, 3),
    "Hidalgo": (-1, 2),
    "Bellas Artes": (1, 2),
    "Allende": (3, 2),
    "Zócalo/Tenochtitlan": (5, 2),
    "San Antonio Abad": (5, -1),
    "Chabacano": (5, -4),
    "Viaducto": (5, -6),
    "Xola": (5, -8),
    "Villa de Cortés": (5, -10),
    "Nativitas": (5, -12),
    "Portales": (5, -14),
    "Ermita": (5, -16),
    "General Anaya": (5, -18),
    "Tasqueña": (5, -20),

    # ================= LINEA 3 (VERDE OLIVO) =================
    "Indios Verdes": (0, 16),
    "Deportivo 18 de Marzo": (0, 14),
    "Potrero": (0, 12),
    "La Raza": (0, 10),
    "Tlatelolco": (0, 8),
    "Guerrero": (0, 6),
    "Juárez": (0, 4),
    "Niños Héroes": (0, -2),
    "Hospital General": (0, -4),
    "Centro Médico": (0, -7),  # <--- ¡AQUÍ ESTABA EL ERROR (FALTABA)!
    "Etiopía/Plaza de la Transparencia": (0, -9),
    "Eugenia": (0, -11),
    "División del Norte": (0, -13),
    "Zapata": (0, -15),
    "Coyoacán": (0, -17),
    "Viveros/Derechos Humanos": (0, -19),
    "Miguel Ángel de Quevedo": (0, -21),
    "Copilco": (0, -23),
    "Universidad": (0, -25),

    # ================= LINEA 4 (AQUA) =================
    "Martín Carrera": (9, 14),
    "Talismán": (9, 12),
    "Bondojito": (9, 10),
    "Consulado": (9, 8),
    "Canal del Norte": (9, 6),
    "Morelos": (9, 4),
    "Fray Servando": (9, 1),
    "Jamaica": (9, -4),
    "Santa Anita": (9, -7),

    # ================= LINEA 5 (AMARILLA) =================
    "Politécnico": (-6, 13),
    "Instituto del Petróleo": (-3, 11),
    "Autobuses del Norte": (-2, 10),
    "Misterios": (-1, 9),
    "Valle Gómez": (3, 9),
    "Eduardo Molina": (11, 8),
    "Aragón": (13, 8),
    "Oceanía": (15, 8),
    "Terminal Aérea": (18, 7),
    "Hangares": (21, 5),

    # ================= LINEA 6 (ROJA) =================
    "El Rosario": (-13, 10),
    "Tezozómoc": (-11, 10),
    "UAM-Azcapotzalco": (-9, 10),
    "Ferrería/Arena Ciudad de México": (-7, 10),
    "Norte 45": (-5, 10),
    "Vallejo": (-3, 11),
    "Lindavista": (2, 13),
    "La Villa-Basílica": (6, 14),

    # ================= LINEA 7 (NARANJA) =================
    "Aquiles Serdán": (-13, 8),
    "Camarones": (-13, 6),
    "Refinería": (-13, 4),
    "San Joaquín": (-13, 2),
    "Polanco": (-13, 1),
    "Auditorio": (-13, 0),
    "Constituyentes": (-13, -1),
    "San Pedro de los Pinos": (-13, -3),
    "San Antonio": (-13, -5),
    "Mixcoac": (-13, -8),
    "Barranca del Muerto": (-13, -11),

    # ================= LINEA 8 (VERDE) =================
    "Garibaldi/Lagunilla": (1, 6),
    "San Juan de Letrán": (1, -1),
    "Doctores": (1, -3),
    "Obrera": (3, -4),
    "La Viga": (7, -6),
    "Coyuya": (10, -7),
    "Iztacalco": (12, -8),
    "Apatlaco": (14, -9),
    "Aculco": (16, -10),
    "Escuadrón 201": (18, -11),
    "Atlalilco": (20, -12),
    "Iztapalapa": (22, -13),
    "Cerro de la Estrella": (24, -14),
    "UAM-I": (26, -15),
    "Constitución de 1917": (28, -16),

    # ================= LINEA 9 (CAFÉ) =================
    "Patriotismo": (-11, -2),
    "Chilpancingo": (-5, -3),
    "Lázaro Cárdenas": (1, -4),
    "Mixiuhca": (11, -4),
    "Velódromo": (14, -4),
    "Ciudad Deportiva": (17, -4),
    "Puebla": (20, -4),

    # ================= LINEA A (MORADA) =================
    "Agrícola Oriental": (27, -1),
    "Canal de San Juan": (30, -2),
    "Tepalcates": (33, -3),
    "Guelatao": (36, -4),
    "Peñón Viejo": (39, -5),
    "Acatitla": (42, -6),
    "Santa Marta": (45, -7),
    "Los Reyes": (48, -8),
    "La Paz": (52, -9),

    # ================= LINEA B (GRIS) =================
    "Buenavista": (-1, 8),
    "Lagunilla": (1, 7),
    "Tepito": (3, 7),
    "Ricardo Flores Magón": (11, 6),
    "Romero Rubio": (13, 6),
    "Deportivo Oceanía": (16, 7),
    "Bosque de Aragón": (19, 8),
    "Villa de Aragón": (22, 9),
    "Nezahualcóyotl": (25, 10),
    "Impulsora": (28, 11),
    "Río de los Remedios": (31, 12),
    "Múzquiz": (34, 13),
    "Ecatepec": (37, 14),
    "Olímpica": (40, 15),
    "Plaza Aragón": (43, 16),
    "Ciudad Azteca": (46, 17),

    # ================= LINEA 12 (DORADA) =================
    "Insurgentes Sur": (-10, -8),
    "Hospital 20 de Noviembre": (-8, -9),
    "Parque de los Venados": (-4, -11),
    "Eje Central": (-1, -13),
    "Mexicaltzingo": (6, -14),
    "Culhuacán": (11, -14),
    "San Andrés Tomatlán": (14, -14),
    "Lomas Estrella": (17, -14),
    "Calle 11": (20, -14),
    "Periférico Oriente": (23, -14),
    "Tezonco": (26, -14),
    "Olivos": (29, -14),
    "Nopalera": (32, -14),
    "Zapotitlán": (35, -14),
    "Tlaltenco": (38, -14),
    "Tláhuac": (42, -14)
}

for nodo in G.nodes():
    if nodo not in pos:
        pos[nodo] = (
            30 + hash(nodo) % 20,
            hash(nodo[::-1]) % 20
        )

# 3. Colores oficiales de cada línea del Metro CDMX
colores_metro = {
    "Línea 1": "#F04E98",  # Rosa
    "Línea 2": "#005EB8",  # Azul
    "Línea 3": "#AF9800",  # Verde olivo
    "Línea 4": "#6BBBAE",  # Cian
    "Línea 5": "#FFD100",  # Amarillo
    "Línea 6": "#DA291C",  # Rojo
    "Línea 7": "#E87722",  # Naranja
    "Línea 8": "#009A44",  # Verde
    "Línea 9": "#512F2E",  # Café
    "Línea A": "#981D97",  # Morado
    "Línea B": "#B1B3B3",  # Gris/Verde
    "Línea 12": "#C99700"  # Dorado
}

# Obtener el color de cada conexión (si creaste el grafo con la Opción A)
colores_aristas = [
    colores_metro.get(G[u][v].get("linea"), "gray") for u, v in G.edges()
]


nx.draw_networkx_edges(
    G,
    pos,
    edge_color=colores_aristas,
    width=3
)

nx.draw_networkx_nodes(
    G,
    pos,
    node_size=40,
    node_color="white",
    edgecolors="black"
)

nx.draw_networkx_labels(
    G,
    pos,
    font_size=5,
    font_color="black"
)

plt.title("Red del Metro CDMX", fontsize=20)
plt.show()
