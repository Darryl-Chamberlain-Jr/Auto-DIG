# SCATTERPLOT
def generate20randomPoints(type):
    arrayOfPoints=[(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
    sigma=1
    leadingCoefficient=(-1)**ZZ.random_element(0, 2)
    T=RealDistribution('gaussian', sigma)
    if type=='linear':
        for i in range(30):
            value=randrange(-10, 10, 1)
            randomness=T.get_random_element()
            arrayOfPoints[i] = (value, (leadingCoefficient*value)+randomness)
    elif type=='power':
        randomPower=ZZ.random_element(2, 6)
        for i in range(30):
            value=RR.random_element(-10, 10)
            randomness=T.get_random_element()
            arrayOfPoints[i] = (value/2, leadingCoefficient*(value/2)**randomPower+randomness)
    elif type=='log':
        for i in range(30):
            value=RR.random_element(0.1, 10)
            randomness=T.get_random_element()
            arrayOfPoints[i] = (value, leadingCoefficient*log(value)+randomness/10)
    elif type=='exp':
        for i in range(30):
            value=RR.random_element(-10, 10)
            randomness=T.get_random_element()
            arrayOfPoints[i] = (value, leadingCoefficient*exp(value)+randomness/10)
    else:
        arrayOfPoints=[(random(), random()) for _ in range(30)]
    return arrayOfPoints

type=['linear', 'power', 'log', 'exp', 'none']
scatterplot=list_plot(generate20randomPoints(type[ZZ.random_element(0,5)]), size=40, color='blue', fontsize=15)
scatterplot.save('muchSuccess.png')

# FUNCTION
#temp = plot(x^2, (x,0,10), color='blue')
#temp.save('moreSuccess.png')

#MULTIPLE FUNCTIONS?
F = tmp_filename(ext='.png')
L = [plot(sin(k*x), (x,-pi,pi)) for k in [1..3]]
G = graphics_array(L)
G.save(F, dpi=500, axes=False)
