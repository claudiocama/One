def config(var):
    with open("config.txt") as file_config:
        for line in file_config:
            if line[0] != "#":
                config_line = line.split("=")
                if config_line[0] == var:
                    ret = config_line[1].replace('"','').replace("\n","")
                    return ret
