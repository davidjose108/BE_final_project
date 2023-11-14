from tarotdeck import TarotCard


class TarotJournal:
    backendAddress = "http://localhost:4557/characters"

    exampleCard1 = TarotCard(
        name="The Fool",
        number=0,
        element="Air",
        raidersmith=False,
        crowley=False,
        description="The begining",
        keywords=["start", "potential", "possibility"],
        journal="",
        occurancy=0,
    )

    exampleCard2 = TarotCard(
        name="The Magician",
        number=1,
        element="Fire",
        raidersmith=False,
        crowley=False,
        description="The play",
        keywords=["intuition", "choice", "impetu"],
        journal="",
        occurancy=0,
    )
