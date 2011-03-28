# Create your views here.
from django.db.models import get_model
from django.shortcuts import render_to_response


"""
Orientation Def

    N
    |
 W--+--O
    |
    S
"""
def laby(request):

    player = get_model('labyrinth', 'player')
    labyrinth = get_model('labyrinth', 'labyrinth')
    results = []
    success = False
    plr = player()
    lab = labyrinth()
    
    qs = request.META['QUERY_STRING']

    if qs is not None:    
        path = list(qs)
    
        for waypoint in path:
            
            if waypoint not in ['V', 'R', 'H', 'L']:
                break
            
            point = lab.checkMove(plr, waypoint)
            results.append(point)
            if point == '0':
                break
            elif point == 'E':
                success = True
                break
            
        
    return render_to_response('labyrinth.html', {'results': results, 'success': success, 'lab': lab, 'plr': plr})

