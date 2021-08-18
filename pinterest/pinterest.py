import json
from typing import List

import requests


class PinterestImage:
    def __init__(self, title: str, pin_id: int, image_id: int, url: str, width: int, height: int) -> None:
        self.title = title
        self.pin_id = pin_id
        self.image_id = image_id
        self.url = url
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f"<PinterestImage title='{self.title}' size='{self.width}x{self.height}'>"

    def __repr__(self) -> str:
        return str(self)


class Pinterest:
    def get_images_by_name(name: str) -> List[PinterestImage]:
        """Busca imagens pelo nome

        Args:
            name (str): nome a ser buscado

        Returns:
            List[PinterestImage]: lista de imagens encontradas
        """

        params = {
            "q": name,
            "rs": "typed",
            "data": json.dumps({"options": {"article": None, "appliedProductFilters": "---", "auto_correction_disabled": False, "corpus": None, "customized_rerank_type": None, "filters": None, "query": "couple anime", "query_pin_sigs": None, "redux_normalize_feed": True, "rs": "typed", "scope": "pins", "source_id": None, "no_fetch_context_on_resource": False}, "context": {}})
        }

        response = requests.get(
            'https://br.pinterest.com/resource/BaseSearchResource/get/?source_url=/search/pins/', params=params)

        response_json = response.json()
        results = response_json["resource_response"]["data"]["results"]

        images = []

        for result in results:
            carousel = result["carousel_data"]

            if not carousel:
                continue

            slots = carousel["carousel_slots"]

            for slot in slots:
                last_resolution = list(slot["images"].keys())[-1]
                best_image_resolution = slot["images"][last_resolution]

                image = PinterestImage(title=slot["title"], pin_id=slot["id"], image_id=slot["id"], url=best_image_resolution["url"],
                                       width=best_image_resolution["width"], height=best_image_resolution["height"])

                images.append(image)

        return images
