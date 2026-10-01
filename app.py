from dash import Dash, html, dcc, Input, Output


# =========================================================
# CONFIGURATION GENERALE
# =========================================================

APP_TITLE = "Ikram Abouzayd | Portfolio"

EMAIL = "ikramabz44@gmail.com"

GITHUB_URL = "https://github.com/ikramabz"




PROJECT_CATEGORIES = [

    # -----------------------------------------------------
    # 01 - ECONOMETRIE
    # -----------------------------------------------------

    {
        "id": "econometrie",
        "number": "01",
        "title": "Économétrie & analyse de données",
        "subtitle": (
            "Analyse statistique, économétrie appliquée "
            "et exploitation de données."
        ),

        "projects": [

            {
                "title": "Analyse de données descriptive",

                "description": (
                    "Analyse des conditions de vie dans les pays "
                    "de l’OCDE à partir des données de 2017."
                ),

                "note": "18,5 / 20",

                "tags": [
                    "Analyse descriptive",
                    "Statistiques",
                    "Analyse en composantes principales (ACP)"
                ],

                "url": "/assets/pdfs/analyse_descriptive.pdf",

                "action": "Voir le rapport PDF",
            },


            {
                "title": "Économétrie linéaire",

                "description": (
                    "Étude des disparités départementales du taux "
                    "d’accidents mortels sur les routes de France."
                ),

                "note": "16,5 / 20",

                "tags": [
                    "Régression linéaire (MCO)",
                    "Sélection de variables",
                    "Prévision"
                ],

                "url": "/assets/pdfs/econometrie_lineaire.pdf",

                "action": "Voir le rapport PDF",
            },

        ],
    },


    # -----------------------------------------------------
    # 02 - BIOSTATISTIQUE
    # -----------------------------------------------------

    {
        "id": "biostatistique",
        "number": "02",
        "title": "Biostatistique",

        "subtitle": (
            "Analyse et traitement des données manquantes, méthodes d’imputation et préparation des données pour l’analyse statistique."
           
        ),

        "projects": [

            {
                "title": "Biostatistique",

                "description": (
                    "Sommeil des mammifères : exploration, analyse "
                    "et traitement des données manquantes."
                ),

                "note": "17,5 / 20",

                "tags": [
                    "Données manquantes",
                    "Imputation multivariée",
                    "Analyse de données"
                ],

                "url": "/assets/pdfs/biostatistique.pdf",

                "action": "Voir le rapport PDF",
            },

        ],
    },


    # -----------------------------------------------------
# 03 - DATA SCIENCE
# -----------------------------------------------------

{
    "id": "datascience",
    "number": "03",
    "title": "Data science & prévision",

    "subtitle": (
        "Méthodes multivariées, modélisation statistique "
        "et séries temporelles."
    ),

    "projects": [

        {
            "title": "Modélisation des variables latentes",

            "description": (
                "Analyse multivariée des conditions de vie "
                "dans les pays de l’OCDE."
            ),

            "note": "18 / 20",

            "tags": [
                "Réduction dimensionnelle",
                "Régression PLS",
                "Classification supervisée"
            ],

            "url": "/assets/pdfs/variables_latentes.pdf",

            "action": "Voir le rapport PDF",
        },


        {
            "title": "Techniques de prévision et conjoncture",

            "description": (
                "Étude et prévision des ventes de véhicules "
                "aux États-Unis à partir de séries temporelles."
            ),

            "note": "16,5 / 20",

            "tags": [
                "Séries temporelles",
                "Prévision",
                "Désaisonnalisation"
            ],

            "url": "/assets/pdfs/prevision_conjoncture.pdf",

            "action": "Voir le rapport PDF",
        },


        # Nouveau projet
        {
            "title": "Régressions pénalisées et sélection de variables",

            "description": (
                "Modélisation du PIB canadien à partir de données "
                "macroéconomiques mensuelles."
            ),

            "note": "En cours",

            "tags": [
                "Régressions pénalisées",
                "Sélection de variables",
                "Données macroéconomiques"
            ],

            "url": None,

            "action": "Rapport à venir",
        },

    ],
},

    # -----------------------------------------------------
    # 04 - FINANCE
    # -----------------------------------------------------

    {
        "id": "finance",
        "number": "04",
        "title": "Finance",

        "subtitle": (
            "Analyse financière, risque, rendement "
            "et évaluation des actifs."
        ),

        "projects": [

            {
                "title": "Évaluation des actifs financiers",

                "description": (
                    "Analyse du risque et du rendement appliquée "
                    "au secteur de l’agriculture."
                ),

                "note": "19 / 20",

                "tags": [
                    "Finance",
                    "Risque",
                    "Rendement"
                ],

                "url": "/assets/pdfs/actifs_financiers.pdf",

                "action": "Voir le rapport PDF",
            },

        ],
    },


]


# =========================================================
# CREATION DE L'APPLICATION DASH
# =========================================================


app = Dash(

    __name__,

    title=APP_TITLE,

    suppress_callback_exceptions=True,

    meta_tags=[

        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1",
        }

    ],
)


# ---------------------------------------------------------
# SERVEUR POUR RENDER / GUNICORN
# ---------------------------------------------------------

server = app.server


# =========================================================
# BARRE DE NAVIGATION
# =========================================================


def navbar():

    return html.Header(

        html.Div(

            [

                # NOM

                dcc.Link(

                    "IKRAM ABOUZAYD",

                    href="/",

                    className="brand",

                ),


                # MENU

                html.Nav(

                    [

                        dcc.Link(
                            "Accueil",
                            href="/",
                            className="nav-link",
                        ),

                        dcc.Link(
                            "Projets",
                            href="/projets",
                            className="nav-link",
                        ),

                        dcc.Link(
                            "Qui suis-je ?",
                            href="/presentation",
                            className="nav-link",
                        ),

                        dcc.Link(
                            "Contact",
                            href="/contact",
                            className="nav-link",
                        ),

                    ],

                    className="main-nav",

                    **{
                        "aria-label": "Navigation principale"
                    },

                ),

            ],

            className="nav-container",

        ),

        className="site-header",

    )


# =========================================================
# PETITE ETIQUETTE POUR LES TECHNOLOGIES
# =========================================================


def tag_badge(text):

    return html.Span(

        text,

        className="tag",

    )


# =========================================================
# CARTE D'UN PROJET
# =========================================================


def project_card(project):

    return html.Article(

        [

            # -------------------------------------------------
            # PARTIE GAUCHE
            # -------------------------------------------------

            html.Div(

                [

                    html.H3(

                        project["title"],

                        className="project-title",

                    ),


                    html.P(

                        project["description"],

                        className="project-description",

                    ),


                    # TECHNOLOGIES

                    html.Div(

                        [

                            tag_badge(tag)

                            for tag in project["tags"]

                        ],

                        className="tag-list",

                    ),

                ],

                className="project-main",

            ),


            # -------------------------------------------------
            # PARTIE DROITE
            # NOTE + BOUTON
            # -------------------------------------------------

            html.Div(

                [

                    # NOTE

                    html.Div(

                        [

                            html.Span(

                                "NOTE",

                                className="note-label",

                            ),

                            html.Strong(

                                project["note"],

                                className="note-value",

                            ),

                        ],

                        className="note-block",

                    ),


                    # BOUTON

                    html.A(

                        [

                            project["action"],

                            html.Span(

                                "↗",

                                className="external-arrow",

                            ),

                        ],

                        href=project["url"],

                        target="_blank",

                        rel="noopener noreferrer",

                        className="project-button",

                    ),

                ],

                className="project-actions",

            ),

        ],

        className="project-card",

    )


# =========================================================
# SECTION D'UNE CATEGORIE
# =========================================================


def category_section(category):

    return html.Section(

        [

            # TITRE DE LA CATEGORIE

            html.Div(

                [

                    html.P(

                        (
                            f'{category["number"]} — '
                            f'{category["title"].upper()}'
                        ),

                        className="section-kicker",

                    ),


                    html.H2(

                        category["title"],

                        className="section-title",

                    ),


                    html.P(

                        category["subtitle"],

                        className="section-subtitle",

                    ),

                ],

                className="section-heading",

            ),


            # PROJETS DE LA CATEGORIE

            html.Div(

                [

                    project_card(project)

                    for project in category["projects"]

                ],

                className="project-list",

            ),

        ],

        id=category["id"],

        className="project-section",

    )


# =========================================================
# FOOTER
# =========================================================


def footer():

    return html.Footer(

        html.Div(

            [

                html.Span(
                    "© Ikram Abouzayd"
                ),

                html.Span(
                    "Portfolio Python · Dash · GitHub"
                ),

            ],

            className="footer-content",

        ),

        className="site-footer",

    )

# =========================================================
# PAGE 1 : ACCUEIL
# =========================================================

def home_page():

    return html.Main(
        [

            # =================================================
            # HERO / PRESENTATION
            # =================================================

            html.Section(
                [

                    # -----------------------------------------
                    # PARTIE GAUCHE
                    # -----------------------------------------

                    html.Div(
                        [

                            # PETIT TITRE

                            html.P(
                                (
                                    "ÉCONOMÉTRIE APPLIQUÉE · "
                                    "ANALYSE DE DONNÉES · "
                                    "MODÉLISATION"
                                ),
                                className="eyebrow",
                            ),


                            # PETITE LIGNE BLEUE

                            html.Div(
                                className="blue-line"
                            ),


                            # NOM

                            html.H1(
                                [
                                    "Ikram ",

                                    html.Span(
                                        "Abouzayd",
                                        className="blue-text",
                                    ),
                                ],
                                className="hero-title",
                            ),


                            # DESCRIPTION

                            html.P(
                                (
                                    "Je m’intéresse aux problématiques où "
                                    "l’analyse permet de mieux comprendre "
                                    "une situation, d’identifier des tendances "
                                    "et d’appuyer la prise de décision. "
                                    "À travers ce portfolio, je présente une "
                                    "sélection de travaux qui illustrent ma "
                                    "démarche, ma rigueur et ma capacité à "
                                    "restituer des résultats de manière claire "
                                    "et structurée."
                                ),
                                className="hero-description",
                            ),


                            # ---------------------------------
                            # BOUTONS
                            # ---------------------------------

                            html.Div(
                                [

                                    # BOUTON PROJETS

                                    dcc.Link(
                                        "Découvrir mes projets",
                                        href="/projets",
                                        className=(
                                            "button "
                                            "button-primary"
                                        ),
                                    ),


                                    # BOUTON CONTACT

                                    dcc.Link(
                                        "Me contacter",
                                        href="/contact",
                                        className=(
                                            "button "
                                            "button-secondary"
                                        ),
                                    ),

                                ],
                                className="hero-buttons",
                            ),

                        ],
                        className="hero-copy",
                    ),


                    # =========================================
                    # CARTE PROFIL A DROITE
                    # =========================================

                    html.Aside(
                        [

                            # ---------------------------------
                            # INITIALES
                            # ---------------------------------
                             html.Div(
                                 html.Img(
                                     src="/assets/photo.png",
                                     className="sidebar-photo",
                                ),
                                className="initials",
                            ),
   

                            # ---------------------------------
                            # TITRE PROFIL
                            # ---------------------------------

                            html.P(
                                "PROFIL",
                                className="card-kicker",
                            ),


                            # ---------------------------------
                            # FORMATION
                            # ---------------------------------

                            html.H2(
                                "Master 2 Économétrie Appliquée",
                                className="profile-title",
                            ),


                            html.P(
                                "IAE Nantes",
                                className="profile-school",
                            ),


                            # SEPARATION

                            html.Div(
                                className="profile-divider"
                            ),


                            # =================================
                            # COMPETENCES TRANSVERSALES
                            # =================================

                            html.Div(
                                [

                                    html.Span(
                                        "Compétences transversales",
                                        className="profile-label",
                                    ),

                                    html.P(
                                        (
                                            "Analyse quantitative · "
                                            "Traitement des données · "
                                            "Modélisation · "
                                            "Visualisation · "
                                            "Synthèse"
                                        ),
                                        className="profile-value",
                                    ),

                                ],
                                className="profile-item",
                            ),


                            # =================================
                            # OUTILS
                            # =================================

                            html.Div(
                                [

                                    html.Span(
                                        "Outils",
                                        className="profile-label",
                                    ),

                                    html.P(
                                        (
                                            "Python · SQL · R · "
                                            "GitHub · Power BI · "
                                            "R Shiny"
                                        ),
                                        className="profile-value",
                                    ),

                                ],
                                className="profile-item",
                            ),


                            # =================================
                            # ATOUTS
                            # =================================

                            html.Div(
                                [

                                    html.Span(
                                        "Atouts",
                                        className="profile-label",
                                    ),

                                    html.P(
                                        (
                                            "Sens du détail · "
                                            "Proactivité · "
                                            "Curiosité analytique · "
                                            "Adaptabilité"
                                        ),
                                        className="profile-value",
                                    ),

                                ],
                                className="profile-item",
                            ),

                        ],
                        className="profile-card",
                    ),

                ],
                className="hero container",
            ),

            

        ]
    )


# =========================================================
# PAGE 2 : PROJETS
# =========================================================


def projects_page():

    # -----------------------------------------------------
    # CREATION AUTOMATIQUE DES BOUTONS DE CATEGORIES
    # -----------------------------------------------------

    category_links = [

        html.A(

            category["title"],

            href=f'#{category["id"]}',

            className="category-chip",

        )

        for category in PROJECT_CATEGORIES

    ]


    return html.Main(

        [

            # -------------------------------------------------
            # INTRODUCTION
            # -------------------------------------------------

            html.Section(

                [


                    html.H1(

                        "Mes projets",

                        className="page-title",

                    ),


                    html.P(

                        (
                            "Une sélection de travaux réalisés "
                            "durant mon Master 1. Chaque projet "
                            "présente le sujet étudié, les méthodes "
                            "mobilisées, la note obtenue et un accès "
                            "direct au rapport ou au projet."
                        ),

                        className="page-intro",

                    ),


                    # -----------------------------------------
                    # BOUTONS DES CATEGORIES
                    # -----------------------------------------

                    html.Div(

                        category_links,

                        className="category-nav",

                    ),

                ],

                className="projects-intro container",

            ),


            # -------------------------------------------------
            # TOUTES LES CATEGORIES
            # -------------------------------------------------

            html.Div(

                [

                    category_section(category)

                    for category in PROJECT_CATEGORIES

                ],

                className="container projects-content",

            ),

        ]

    )


# =========================================================
# PAGE 3 : PRESENTATION
# =========================================================

presentation_page = html.Main(
    [
        html.Div(
            [
                html.P(
                    "PRÉSENTATION",
                    className="eyebrow",
                ),

                html.H1(
                    "À propos de moi",
                    className="page-title",
                ),

                html.P(
                    "Cette vidéo présente mon parcours autrement : ma personnalité, mes centres d’intérêt et ce qui nourrit aujourd’hui mon intérêt pour l’analyse de données.",
                    className="page-intro",
                ),

                html.Video(
                    src="/assets/presentation.mp4",
                    controls=True,
                    className="presentation-video",
                ),
            ],
            className="container presentation-page",
        )
    ]
)


# =========================================================
# PAGE 4 : CONTACT
# =========================================================


def contact_page():

    return html.Main(

        html.Section(

            [

                html.P(

                    "CONTACT",

                    className="eyebrow",

                ),


                html.H1(

                    "Échangeons",

                    className="page-title",

                ),


                html.P(

                    (
                        "Vous souhaitez échanger à propos "
                        "de mon profil, de mes travaux "
                        "académiques ou d’une opportunité "
                        "professionnelle ? Vous pouvez me "
                        "contacter directement."
                    ),

                    className="page-intro",

                ),




                # ---------------------------------------------
                # CARTE CONTACT
                # ---------------------------------------------

                html.Div(

                    [

                        # EMAIL

                        html.Div(

                            [

                                html.Span(

                                    "E-MAIL",

                                    className="contact-label",

                                ),


                                html.A(

                                    EMAIL,

                                    href=f"mailto:{EMAIL}",

                                    className="contact-value",

                                ),

                            ],

                            className="contact-row",

                        ),


                        # GITHUB

                        html.Div(

                            [

                                html.Span(

                                    "GITHUB",

                                    className="contact-label",

                                ),


                                html.A(

                                    "github.com/ikramabz",

                                    href=GITHUB_URL,

                                    target="_blank",

                                    rel="noopener noreferrer",

                                    className="contact-value",

                                ),

                            ],

                            className="contact-row",

                        ),

                    ],

                    className="contact-card",

                ),


                # ---------------------------------------------
                # BOUTONS CONTACT
                # ---------------------------------------------

                html.Div(

                    [

                        html.A(
                            "Envoyer un e-mail",
                            href=f"https://mail.google.com/mail/?view=cm&fs=1&to={EMAIL}",
                            target="_blank",
                            className=(
                            "button "
                            "button-primary"
                        ),
                        

                        ),


                        dcc.Link(

                            "Voir mes projets",

                            href="/projets",

                            className=(
                                "button "
                                "button-secondary"
                            ),

                        ),

                    ],

                    className="contact-actions",

                ),

            ],

            className="contact-page container",

        )

    )


# =========================================================
# STRUCTURE GENERALE DU SITE
# =========================================================


app.layout = html.Div(

    [

        # URL ACTUELLE

        dcc.Location(

            id="url",

            refresh=False,

        ),


        # BARRE DE NAVIGATION

        navbar(),


        # ENDROIT OU LA PAGE EST AFFICHEE

        html.Div(

            id="page-content"

        ),


        # PIED DE PAGE

        footer(),

    ],

    className="app-shell",

)


# =========================================================
# NAVIGATION ENTRE LES PAGES
# =========================================================


@app.callback(

    Output(
        "page-content",
        "children"
    ),

    Input(
        "url",
        "pathname"
    ),

)

def render_page(pathname):

    # Permet d'accepter /projets et /projets/

    path = (
        (pathname or "/")
        .rstrip("/")
        or "/"
    )

    # PAGE PROJETS

    if path == "/projets":
        return projects_page()

    # PAGE PRESENTATION

    if path == "/presentation":
        return presentation_page

    # PAGE CONTACT

    if path == "/contact":
        return contact_page()

    # PAR DEFAUT = ACCUEIL

    return home_page()

# =========================================================
# LANCEMENT LOCAL
# =========================================================


if __name__ == "__main__":

    app.run(
        debug=True
    )