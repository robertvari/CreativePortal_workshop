from datetime import datetime


def get_posts(number: int) -> list:
    post_list = []

    for index in range(number):
        post_list.append(
            {
                "title": "Post Title",
                "user": "User Name",
                "image": f"https://source.unsplash.com/1600x900/?nature{index}",
                "date": datetime.now()
            }
        )

    return post_list
