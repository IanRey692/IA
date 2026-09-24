import math
import heapq

def heuristica_Euclidiana(nodo_actual, nodo_destino, grafo):
    """Heuristica euclidiana"""

    x1=grafo.nodes[nodo_actual]['x']
    y1=grafo.nodes[nodo_actual]['y']
    x2=grafo.nodes[nodo_destino]['x']
    y2=grafo.nodes[nodo_destino]['y']
    distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)*111000
    return distancia

def heuristica_Haversine(nodo_actual, nodo_destino, grafo):
    """"Heuristica Haversine"""
    lon1=math.radians(grafo.nodes[nodo_actual]['x'])
    lat1=math.radians(grafo.nodes[nodo_actual]['y'])
    lon2=math.radians(grafo.nodes[nodo_destino]['x'])
    lat2=math.radians(grafo.nodes[nodo_destino]['y'])

    dlon=lon2-lon1
    dlat=lat2-lat1
    a=math.sin(dlat/2)**2+math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c=2*math.atan2(math.sqrt(a),math.sqrt(1-a))

    radio_tierra=6371000
    distancia=radio_tierra*c
    return distancia
def heuristica_personalizada(nodo_actual, nodo_destino, grafo):
    dis_base=heuristica_Haversine(nodo_actual, nodo_destino, grafo )
    num_giros=dis_base/100
    costop_giro=15
    h_final=dis_base+(num_giros*costop_giro)
    return h_final
def algo_estrella(grafo, origen, destino, heuristica):
    frontera=[]
    heapq.heappush(frontera,(0,0,origen,[origen]))
    costo_real={origen:0}
    nodos_rev=0
    while len(frontera)>0:
        f_n, g_n,actual,camino=heapq.heappop(frontera)
        nodos_rev+=1
        if actual==destino:
            return{
                "camino": camino,
                "metros": g_n,
                "nodos_expandidos": nodos_rev
            }
        for vecino in grafo.neighbors(actual):
            try:
                peso_arista=grafo[actual][vecino][0].get('length',10)
            except:
                peso_arista=10
            costo_g_nuevo=g_n+peso_arista
            if vecino not in costo_real or costo_g_nuevo<costo_real[vecino]:
                costo_real[vecino]=costo_g_nuevo
                h_n=heuristica(vecino,destino,grafo)
                f_n_nuevo=costo_g_nuevo+h_n

                heapq.heappush(frontera,(f_n_nuevo,costo_g_nuevo,vecino,camino+[vecino]))
    return None

#Greedy

def algo_greedy(grafo, origen,destino,heuristica):
    """Greedy Best-Firts(solo h, sin g) y comparar contra A"""
    frontera=[]
    heapq.heappush(frontera,(0,origen,[origen],0))
    visitados=set()
    nodos_rev=0
    while len(frontera)>0:
        h_n,actual,camino,g_n=heapq.heappop(frontera)
        nodos_rev+=1
        if actual==destino:
            return {
                "camino": camino,
                "metros": g_n,
                "nodos_expandidos": nodos_rev
            }

        if actual in visitados:
            continue
            
        visitados.add(actual)

        for vecino in grafo.neighbors(actual):
            if vecino not in visitados:
                try:
                    peso_arista = grafo[actual][vecino][0].get('length', 10)
                except:
                    peso_arista = 10
                    
                costo_g_nuevo = g_n + peso_arista
                h_vecino = heuristica(vecino, destino, grafo)
                
                heapq.heappush(frontera, (h_vecino, vecino, camino + [vecino], costo_g_nuevo))

    return None
