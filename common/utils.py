from sh import sed


def logi(title, msg):
    #print( "[info] => " + msg )
    print("\n[info] => {}\n{}".format(title,msg))



def log(msg):
    print( "[log] => " + msg )

def loge(msg):
    print( "[error] => " + msg )

def replace(old, new, file):
    sed("-i", "s/{}/{}/g".format(old, new), file)
