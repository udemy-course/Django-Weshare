from hashlib import md5

from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):

    user_from = models.ForeignKey(
        to=User,
        related_name='from_set',
        on_delete=models.CASCADE)
    user_to = models.ForeignKey(
        to=User,
        related_name='to_set',
        on_delete=models.CASCADE)
    created = models.DateTimeField(
        auto_now_add=True,
        db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} follows {}'.format(
            self.user_from, self.user_to)


# Add following field to User dynamically
User.add_to_class(
    'following',
    models.ManyToManyField(
        'self',
        through=Contact,
        related_name='followers',
        symmetrical=False)
)


def gravatar(self, size=80):
    md5_digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(md5_digest, size)


User.add_to_class(
    'gravatar',
    gravatar
)
