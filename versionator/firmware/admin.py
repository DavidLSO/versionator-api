from django.contrib import admin
from versionator.firmware.models import Firmware


@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'version', 'compatible_card_name', 'file']
