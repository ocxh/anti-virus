import kavcore.k2engine

k2 = kavcore.k2engine.Engine(debug=True)
if k2.set_plugins('plugins'):
    kav = k2.create_instance()
    if kav:
        print '[*] Success : create_instance'
        