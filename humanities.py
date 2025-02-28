# What counts as a humanities course changes depending on what year you were admitted
# Check degree works if using for yourself

hum = {
    "AAST":{"200", "315"},
    "AFST":{"101", "202"},
    "ARST":{"100", "240", "273", "340"},
    "ARTH":{"101", "102", "103", "104", "105", "190", "210", "212", "213", "214", "215", "222", "225", "231", "241", "242", "243", "250", "254", "260", "261", "263", "265", "275", "277", "278", "280", "285", "287", "290", "294"},
    "ARTM":{"225"},
    "ASST":{"101"},
    "CHST":{"100", "240", "270", "340"},
    "CLAS":{"101", "102", "103", "104", "200", "203", "215", "223", "225", "226", "242", "253", "254", "255", "256", "270", "303", "320", "322", "324", "343", "345", "356"},
    "DANC":{"150", "290", "330", "331"},
    "DCSP":{"350"},
    "EDFS":{"201"},
    "ENGL":{"190", "191", "192", "195", "201", "202", "207", "212", "216", "226", "233", "234", "241", "290", "300", "302", "304", "306", "313", "314", "315", "317", "318", "319", "320", "321", "323", "325", "326", "327", "328", "335", "336", "337", "339", "340", "341", "342", "343", "344", "345", "346", "349", "351", "352", "353", "356", "357", "358", "359", "360", "361", "362", "363", "364", "370", "371", "375", "390"},
    "ENVT":{"210"},
    "FRCS":{"101", "102"},
    "FREN":{"334", "335", "336", "337"},
    "GEOG":{"219", "290"},
    "GRMN":{"325", "326", "329", "365", "390", "468", "472", "490"},
    "GRST":{"122", "200", "221", "222", "223", "231", "270", "271", "371"},
    "HISP":{"250", "251", "252"},
    "HIST":{"201", "202", "210", "211", "212", "213", "215", "216", "217", "218", "219", "222", "224", "225", "226", "228", "229", "230", "231", "232", "234", "235", "241", "242", "244", "247", "248", "249", "250", "251", "252", "253", "255", "257", "261", "262", "263", "270", "272", "273", "276", "277", "291", "301", "302", "304", "310", "320", "323", "335", "336", "337", "341", "343", "344", "345", "346", "347", "348", "350", "357", "361", "364", "370", "403"},
    "HONS":{"170", "172", "175", "281", "381"},
    "HPCP":{"199", "275"},
    "IIAS":{"201", "304"},
    "ITAL":{"361", "362", "390", "452"},
    "ITST":{"390"},
    "JWST":{"201", "220", "225", "230", "240", "242", "245", "260", "300", "305", "310", "315", "320", "325", "330", "335", "350"},
    "LACS":{"101", "103", "104", "105", "106"},
    "LATN":{"305", "321", "322", "323", "371", "372", "373", "390"},
    "LTAR":{"220", "221", "250", "270", "350", "382"},
    "LTCH":{"210", "220", "250"},
    "LTFR":{"150", "250"},
    "LTIT":{"250", "270", "350", "370"},
    "LTJP":{"250", "350", "390"},
    "LTPO":{"150", "250", "270", "280", "350"},
    "LTRS":{"110", "120", "170", "210", "220", "250", "270"},
    "LTSP":{"250", "252"},
    "MEDH":{"200"},
    "MUSC":{"131", "222", "223", "225", "227", "230", "232", "233", "234", "280"},
    "PHIL":{"101", "105", "110", "115", "150", "155", "160", "165", "170", "185", "198", "201", "202", "203", "205", "206", "207", "208", "209", "210", "220", "234", "240", "245", "252", "255", "260", "265", "270", "275", "280", "282", "285", "290", "298"},
    "POLI":{"280"},
    "RELS":{"101", "103", "105", "106", "115", "120", "185", "201", "202", "205", "210", "220", "223", "225", "230", "235", "240", "245", "248", "250", "255", "260", "270", "275", "276", "280", "285", "298"},
    "RUSS":{"390"},
    "RUST":{"200", "250", "300"},
    "SOST":{"175", "200", "241"},
    "SPAN":{"320", "332", "333"},
    "SPOL":{"150"},
    "THTR":{"175", "176", "177", "212", "214", "218", "288", "310", "311", "315", "316", "318", "321", "387", "488"},
    "URST":{"398"},
    "WGST":{"228", "229", "255"}
}

def isHumanClass(c):
    if c["subject"] not in hum: return False
    return c["courseNumber"] in hum[c["subject"]]