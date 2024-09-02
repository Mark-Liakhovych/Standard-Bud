from django.shortcuts import render
from .models import GREEN_OASIS_EN, GREEN_OASIS_DE, GREEN_OASIS_PL, BRIGHT_SIMPLICITY_EN, BRIGHT_SIMPLICITY_DE, BRIGHT_SIMPLICITY_PL, FUTURE_ON_TOP_EN, FUTURE_ON_TOP_DE, FUTURE_ON_TOP_PL, MODERNITY_IN_GLASS_WALLS_EN, MODERNITY_IN_GLASS_WALLS_DE, MODERNITY_IN_GLASS_WALLS_PL, MODERN_TWINS_EN, MODERN_TWINS_DE, MODERN_TWINS_PL, PRIVATE_COSINESS_EN, PRIVATE_COSINESS_DE, PRIVATE_COSINESS_PL, SPACE_FOR_CREATIVITY_EN, SPACE_FOR_CREATIVITY_DE, SPACE_FOR_CREATIVITY_PL, STRICT_ELEGANCE_EN, STRICT_ELEGANCE_DE, STRICT_ELEGANCE_PL

# Create your views here.


def about_us(request):
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }
    return render(request, 'aboutUs.html', context)


def index_pl(request):
    return render(request, 'indexPL.html')


def index_de(request):
    return render(request, 'indexDE.html')


def about_us_de(request):
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }
    return render(request, 'aboutUsDE.html', context)


def about_us_pl(request):
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }
    return render(request, 'aboutUsPL.html', context)


def coming_soon(request):
    return render(request, 'comingSoon.html')


def coming_soon_de(request):
    return render(request, 'comingSoonDE.html')


def coming_soon_pl(request):
    return render(request, 'comingSoonPL.html')


def contact(request):
    return render(request, 'contact.html')


def contact_de(request):
    return render(request, 'contactDE.html')


def contact_pl(request):
    return render(request, 'contactPL.html')


def index(request):
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }
    return render(request, 'index.html', context)


def index_de(request):
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }
    return render(request, 'indexDE.html', context)


def index_pl(request):
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }
    return render(request, 'indexPL.html', context)


def job(request):
    return render(request, 'jop.html')


def job_de(request):
    return render(request, 'jopDE.html')


def job_pl(request):
    return render(request, 'jopPL.html')


def our_projects(request):
    bright_simplicity_model = BRIGHT_SIMPLICITY_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    private_cosiness_model = PRIVATE_COSINESS_EN.objects.all()
    space_for_creativity_model = SPACE_FOR_CREATIVITY_EN.objects.all()
    strict_elegance_model = STRICT_ELEGANCE_EN.objects.all()

    context = {
        'bright_simplicity_model': bright_simplicity_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
        'private_cosiness_model': private_cosiness_model,
        'space_for_creativity_model': space_for_creativity_model,
        'strict_elegance_model': strict_elegance_model,
    }

    return render(request, 'ourProjects.html', context)


def our_projects_de(request):
    bright_simplicity_model = BRIGHT_SIMPLICITY_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    private_cosiness_model = PRIVATE_COSINESS_DE.objects.all()
    space_for_creativity_model = SPACE_FOR_CREATIVITY_DE.objects.all()
    strict_elegance_model = STRICT_ELEGANCE_DE.objects.all()

    context = {
        'bright_simplicity_model': bright_simplicity_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
        'private_cosiness_model': private_cosiness_model,
        'space_for_creativity_model': space_for_creativity_model,
        'strict_elegance_model': strict_elegance_model,
    }

    return render(request, 'ourProjectsDE.html', context)


def our_projects_pl(request):
    bright_simplicity_model = BRIGHT_SIMPLICITY_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    private_cosiness_model = PRIVATE_COSINESS_PL.objects.all()
    space_for_creativity_model = SPACE_FOR_CREATIVITY_PL.objects.all()
    strict_elegance_model = STRICT_ELEGANCE_PL.objects.all()

    context = {
        'bright_simplicity_model': bright_simplicity_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
        'private_cosiness_model': private_cosiness_model,
        'space_for_creativity_model': space_for_creativity_model,
        'strict_elegance_model': strict_elegance_model,
    }

    return render(request, 'ourProjectsPL.html', context)


def bright_simplicity(request):
    bright_simplicity_model = BRIGHT_SIMPLICITY_EN.objects.all()
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()

    context = {
        'bright_simplicity_model': bright_simplicity_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
    }
    return render(request, 'Projects/brightSimplicity.html', context)


def bright_simplicity_de(request):
    bright_simplicity_model = BRIGHT_SIMPLICITY_DE.objects.all()
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()

    context = {
        'bright_simplicity_model': bright_simplicity_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
    }
    return render(request, 'Projects/brightSimplicityDE.html', context)


def bright_simplicity_pl(request):
    bright_simplicity_model = BRIGHT_SIMPLICITY_PL.objects.all()
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()

    context = {
        'bright_simplicity_model': bright_simplicity_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
    }

    return render(request, 'Projects/brightSimplicityPL.html', context)


def future_on_top(request):
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()

    context = {
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
    }

    return render(request, 'Projects/futureOnTop.html', context)


def future_on_top_de(request):
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()

    context = {
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
    }
    return render(request, 'Projects/futureOnTopDE.html', context)


def future_on_top_pl(request):
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()

    context = {
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
    }
    return render(request, 'Projects/futureOnTopPL.html', context)


def green_oasis(request):
    green_oasis_model = GREEN_OASIS_EN.objects.all()
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()

    context = {
        'green_oasis_model': green_oasis_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/greenOasis.html', context)


def green_oasis_de(request):
    green_oasis_model = GREEN_OASIS_DE.objects.all()
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()

    context = {
        'green_oasis_model': green_oasis_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/greenOasisDE.html', context)


def green_oasis_pl(request):
    green_oasis_model = GREEN_OASIS_PL.objects.all()
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()

    context = {
        'green_oasis_model': green_oasis_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/greenOasisPL.html', context)


def modernity_in_glass_walls(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()

    context = {
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
    }

    return render(request, 'Projects/modernityInGlassWalls.html', context)


def modernity_in_glass_walls_de(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()

    context = {
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
    }

    return render(request, 'Projects/modernityInGlassWallsDE.html', context)


def modernity_in_glass_walls_pl(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()

    context = {
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
    }

    return render(request, 'Projects/modernityInGlassWallsPL.html', context)


def modern_twins(request):
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/modernTwins.html', context)


def modern_twins_de(request):
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/modernTwinsDE.html', context)


def modern_twins_pl(request):
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()

    context = {
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/modernTwinsPL.html', context)


def private_cosiness(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()
    private_cosiness_model = PRIVATE_COSINESS_EN.objects.all()
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()

    context = {
        'private_cosiness_model': private_cosiness_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,

    }

    return render(request, 'Projects/privateCosiness.html', context)


def private_cosiness_de(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()
    private_cosiness_model = PRIVATE_COSINESS_DE.objects.all()
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()

    context = {
        'private_cosiness_model': private_cosiness_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,

    }

    return render(request, 'Projects/privateCosinessDE.html', context)


def private_cosiness_pl(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()
    private_cosiness_model = PRIVATE_COSINESS_PL.objects.all()
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()

    context = {
        'private_cosiness_model': private_cosiness_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,

    }

    return render(request, 'Projects/privateCosinessPL.html', context)


def space_for_creativity(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()
    space_for_creativity_model = SPACE_FOR_CREATIVITY_EN.objects.all()
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()

    context = {
        'space_for_creativity_model': space_for_creativity_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,

    }

    return render(request, 'Projects/spaceForCreativity.html', context)


def space_for_creativity_de(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()
    space_for_creativity_model = SPACE_FOR_CREATIVITY_DE.objects.all()
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()

    context = {
        'space_for_creativity_model': space_for_creativity_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/spaceForCreativityDE.html', context)


def space_for_creativity_pl(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()
    space_for_creativity_model = SPACE_FOR_CREATIVITY_PL.objects.all()
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()

    context = {
        'space_for_creativity_model': space_for_creativity_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/spaceForCreativityPL.html', context)


def strict_elegance(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_EN.objects.all()
    strict_elegance_model = STRICT_ELEGANCE_EN.objects.all()
    modern_twins_model = MODERN_TWINS_EN.objects.all()
    future_on_top_model = FUTURE_ON_TOP_EN.objects.all()
    green_oasis_model = GREEN_OASIS_EN.objects.all()

    context = {
        'strict_elegance_model': strict_elegance_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/strictElegance.html', context)


def strict_elegance_de(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_DE.objects.all()
    strict_elegance_model = STRICT_ELEGANCE_DE.objects.all()
    modern_twins_model = MODERN_TWINS_DE.objects.all()
    future_on_top_model = FUTURE_ON_TOP_DE.objects.all()
    green_oasis_model = GREEN_OASIS_DE.objects.all()

    context = {
        'strict_elegance_model': strict_elegance_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/strictEleganceDE.html', context)


def strict_elegance_pl(request):
    modernity_in_glass_walls_model = MODERNITY_IN_GLASS_WALLS_PL.objects.all()
    strict_elegance_model = STRICT_ELEGANCE_PL.objects.all()
    modern_twins_model = MODERN_TWINS_PL.objects.all()
    future_on_top_model = FUTURE_ON_TOP_PL.objects.all()
    green_oasis_model = GREEN_OASIS_PL.objects.all()

    context = {
        'strict_elegance_model': strict_elegance_model,
        'modern_twins_model': modern_twins_model,
        'future_on_top_model': future_on_top_model,
        'green_oasis_model': green_oasis_model,
        'modernity_in_glass_walls_model': modernity_in_glass_walls_model,
    }

    return render(request, 'Projects/strictElegancePL.html', context)
