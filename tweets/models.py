from django.db import models
from common.models import CommonModel


# Create your models here.
class Tweet(CommonModel):
    payload = models.CharField(max_length=180)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.user}]{self.payload}"


class Like(CommonModel):
    tweet = models.ForeignKey("tweets.Tweet", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.user}]{self.tweet}"
