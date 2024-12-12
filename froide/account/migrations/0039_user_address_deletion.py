from django.db import migrations, models

import oauth2_provider.generators
import oauth2_provider.models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0038_application_allowed_origins_and_more"),
    ]

    operations = [
        migrations.RemoveField(
          model_name="user",
          name="address",
        )
    ]
