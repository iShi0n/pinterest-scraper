
from __future__ import annotations
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

    def as_dict(self) -> dict:
        return {
            "title": self.title,
            "pin_id": self.pin_id,
            "image_id": self.image_id,
            "url": self.url
        }


class Pinterest:
    def get_images_by_name(name: str) -> List[Couple]:
        """Busca imagens pelo nome

        Args:
            name (str): nome a ser buscado

        Returns:
            List[PinterestImage]: lista de imagens encontradas
        """

        params = {
            "q": name,
            "rs": "typed",
            "len": 2,
            "data": json.dumps({"options": {"article": None, "page_size": 250, "appliedProductFilters": "---", "auto_correction_disabled": False, "corpus": None, "customized_rerank_type": None, "filters": None, "query": "couple anime", "query_pin_sigs": None, "redux_normalize_feed": True, "rs": "typed", "scope": "pins", "source_id": None, "no_fetch_context_on_resource": False}, "context": {}, "bookmarks": ['Y2JVSG81V2sxcmNHRlpWM1J5VFVad1ZscEhSbE5XYXpVd1dXdFZNVlV3TVZkalNHUlhVak5vY2xWNlNrZFNhelZYWVVaU2FWWkZXbTlXYlhSaFV6SlNSMVZZYUZaaWEzQlFWbXhTYzFKc1ZYaGhTR1JXVW14d1NGVnNVa2RXVmxwWVZXeE9ZVlpXVlhoVk1GcFBaRVV4Vms1V1pGTldiR3Q0Vm1wS05GVXhSblJXYmtwUVZsZG9WRmxzWkc5VU1YQllaRVYwYWxadFVubFdWM1JyWVVaYWRWRnNXbGRXYkVwVVZsVmFTMU5HVm5WVGJGWnBWMFZLUkZkc1pIcGxSMDVYVTJ4V1VtSklRazlaV0hCQ1pVWmFTR05GZEZWTmEzQlhWRlpvVTFZeVJuUmhSbHBhVmtWYWFGWXhXbmRqYkVwVllrWkdWbFpFUVRWYWExcFhVMWRLTmxWdGVGTk5XRUpIVmxSSmVHTXhVbk5UV0doWVltdEtWbGxyWkZOVVJteFdWbFJHV0ZKck5UQlVWbVJIVmpGS2NtTkVRbGRTUlZwVVdUSnpNVlpyT1ZaV2JGSllVMFZLVWxadGRHRlNhekZYVld4YVlWSnJjSE5WYkZKWFUxWlZlVTFJYUZWaVJuQkhWbTF3VjFkSFNrZFRhMDVoVmpOTk1WVXdXa3RrUjBaR1RsZDRhRTFJUWpSV2Frb3dWVEZKZVZKc1pHcFNiRnBYVm10YVMxVldWbkphUms1cVlrWktNRmt3Vmt0aVIwWTJVbTVvVm1KR1NrUldNbk40WTJzeFJWSnNWbWhoTTBKUlYxZDRWbVZIVWtkWGJrWm9VbXhhYjFSV1duZFhiR1IwWkVWYVVGWnJTbE5WUmxGNFQwVXhObE5VVWs5V1IzaHpWRmR3YTJGV2JIUlNXSEJQWWxad2RGZHRNVTVsUlRsVlZWUkdZV0Z0VGpaVWJuQnlUbFUxV0ZKWWFGQldSa3B5Vkd0a1ZrNVdjRlZhUjNSUFRXc3dNRlJ1Y0VKTlZURkZWRzB4VUZZd1ZqVlVibkJhVFVad1NGZFVSbUZTUjJoelZGWmtSbVZXY0ZsbFJUbFRWbTFSTkdaRVVteE5SRUV5VFZkVk1scHRXVE5OVjBwcFRrZEpNVTFYVlRKYVJGVTBUMVJuTVU1RVRtdGFWRkYzV21wTk5WcHFRVEJQVkVsNldXMUpNbGw2Wkd0TlJGRXhUVEpGTTAxRVNUUk5la0Y0V2tkVk0wMXFaRGhVYTFaWVprRTlQUT09fFVIbzVVVk5ZVlhaVlZtUjVWVWQwZDJGNk1XWk5WamgwVFZoM01FOVhWbXRhUkdONldsUnJlRTR5U1RKT2VtTTBXa1JXYWs1VVpHcFpWMFY2V1dwak5FNVVWbWhhYWtKcFdWZFdhbGxxYkd4YWJVMTRUVmRHYVUxcVdUVk9WR1JvVDBkWk5VNXFiRzFOYW1kNlRsZE5OR1pGTlVaV00zYzl8ZDlmNWY2YjNjOWJmY2I2YTIwNDdiZWRjOWI4Mjg2ZGRkYjNmMDkxMzk2MGFhMDUwMTI3NmRjZmNmNmNhMzZmYnxORVd8']})
        }
        response = requests.get(
            'https://br.pinterest.com/resource/BaseSearchResource/get/?source_url=/search/pins/', params=params)

        response_json = response.json()
        results = response_json["resource_response"]["data"]["results"]

        images = []

        for result in results:
            try:
                carousel = result["carousel_data"]
                slots = carousel["carousel_slots"]
            except:
                continue

            children = []

            for slot in slots:
                last_resolution = list(slot["images"].keys())[-1]
                best_image_resolution = slot["images"][last_resolution]

                image = PinterestImage(title=slot["title"], pin_id=slot["id"], image_id=slot["id"], url=best_image_resolution["url"],
                                       width=best_image_resolution["width"], height=best_image_resolution["height"])

                children.append(image)

            images.append(Couple(children))

        return images


class Couple:
    def __init__(self, images: List[PinterestImage]) -> None:
        self.images = images

    def as_dict(self):
        return [
            image.as_dict() for image in self.images
        ]
