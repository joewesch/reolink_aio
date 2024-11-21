"""Reolink Baichuan XML templates."""

XML_HEADER = """<?xml version="1.0" encoding="UTF-8" ?>"""

LOGIN_XML = """<?xml version="1.0" encoding="UTF-8" ?>
<body>
<LoginUser version="1.1">
<userName>{userName}</userName>
<password>{password}</password>
<userVer>1</userVer>
</LoginUser>
<LoginNet version="1.1">
<type>LAN</type>
<udpPort>0</udpPort>
</LoginNet>
</body>
"""

LOGOUT_XML = """<?xml version="1.0" encoding="UTF-8" ?>
<body>
<LoginUser version="1.1">
<userName>{userName}</userName>
<password>{password}</password>
<userVer>1</userVer>
</LoginUser>
</body>
"""

CHANNEL_EXTENSION_XML = """<?xml version="1.0" encoding="UTF-8" ?>
<Extension version="1.1">
<channelId>{channel}</channelId>
</Extension>
"""

DingDongOpt_2_XML = """
<?xml version="1.0" encoding="UTF-8" ?>
<body>
<dingdongDeviceOpt version="1.1">
<id>{chime_id}</id>
<opt>getParam</opt>
</dingdongDeviceOpt>
</body>
"""

DingDongOpt_3_XML = """
<?xml version="1.0" encoding="UTF-8" ?>
<body>
<dingdongDeviceOpt version="1.1">
<opt>setParam</opt>
<id>{chime_id}</id>
<volLevel>{vol}</volLevel>
<ledState>{led}</ledState>
<name>{name}</name>
</dingdongDeviceOpt>
</body>
"""

DingDongOpt_4_XML = """
<?xml version="1.0" encoding="UTF-8" ?>
<body>
<dingdongDeviceOpt version="1.1">
<id>{chime_id}</id>
<opt>{opt}</opt>
</dingdongDeviceOpt>
</body>
"""

SetDingDongCfg_XML = """
<?xml version="1.0" encoding="UTF-8" ?>
<body>
<dingdongCfg version="1.1">
<deviceCfg>
<id>{chime_id}</id>
<alarminCfg>
<valid>{state}</valid>
<musicId>{tone_id}</musicId>
<type>{event_type}</type>
</alarminCfg>
</deviceCfg>
</dingdongCfg>
</body>
"""
