# Let's create the complete static site generator project structure

# First, let's organize the content from the European Mobility Symposium website
content_data = {
    "site": {
        "title": "European Mobility Symposium",
        "subtitle": "Turin, 25-26 September, 2025",
        "description": "The European Mobility Symposium has the goal of sharing insights from recent works on human mobility and exploring new perspectives and potential collaborations—both in terms of research papers and project proposals."
    },
    "event": {
        "venue": "ISI Foundation. Via Chisola, 5, 10126 Turin TO.",
        "dates": "September 25-26, 2025",
        "location_map": "Institute for Scientific Interchange, ISI Foundation"
    },
    "participants": [
        {
            "institution": "Central European University, Austria",
            "people": ["Márton Karsai","Elisa Omodei"]
        },
        {
            "institution": "Corvinus University, Hungary", 
            "people": ["Balázs Lengyel","Gergő Pintér"]
        },
        {
            "institution": "Mobile and Social Computing Lab - Fondazione Bruno Kessler, Trento, Italy",
            "people": ["Massimiliano Luca", "Sebastiano Bontorin", "Bruno Lepri"]
        },
        {
            "institution": "CHuB - Fondazione Bruno Kessler, Trento, Italy",
            "people": ["Riccardo Gallotti", "Andrea Guizzo"]
        },
        {
            "institution": "ISI Foundation, Italy",
            "people": ["Antonio Desiderio","Leo Ferres", "Mattia Mazzoli", "Rossano Schifanella", "Kyriaki Kalimeri"]
        },
        {
            "institution": "ISTI-CNR, Pisa, Italy",
            "people": [
                "Luca Pappalardo (ISTI-CNR and Scuola Normale Superiore, Pisa, Italy)",
                "Mirco Nanni", 
                "Giuliano Cornacchia",
                "Giovanni Mauro (ISTI-CNR and Scuola Normale Superiore, Pisa, Italy)",
                "Paolo De Biase"
            ]
        },
        {
            "institution": "Northeastern University of London, UK",
            "people": ["Riccardo Di Clemente", "Nandini Iyer"]
        },
        {
            "institution": "Sony CSL, Italy",
            "people": ["Vittorio Loreto", "Hygor Piaget Monteiro Melo", "Matteo Bruno"]
        },
        {
            "institution": "Technical University of Denmark, Denmark",
            "people": ["Laura Alessandretti"]
        },
        {
            "institution": "University of Exeter, UK",
            "people": ["Federico Botta","Ronaldo Menezes"]
        },
        {
            "institution": "Wroclaw University of Environmental and Life Sciences, Poland",
            "people": ["Kamil Smolak"]
        },
        {
            "institution": "Insitute for Cross-Disciplinary Physics and Complex Systems, Spain",
            "people": ["Jose Ramasco"]
        },

    ],
    "organizers": {
        "steering_committee": [
            "Luca Pappalardo (ISTI-CNR and Scuola Normale Superiore, Pisa, Italy)",
            "Riccardo Di Clemente (Northeastern University of London, UK)", 
        ],
        "web_chair": "Antonio Desiderio (ISI Foundation, Turin, Italy)",
        "local_chair": "Mattia Mazzoli (ISI Foundation, Turin, Italy)"
    }
}

print("Content data structure created successfully!")
print(f"Site title: {content_data['site']['title']}")
print(f"Number of participating institutions: {len(content_data['participants'])}")