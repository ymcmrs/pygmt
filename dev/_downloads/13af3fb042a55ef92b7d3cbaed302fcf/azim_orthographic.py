"""
Orthographic
============

This is a perspective projection like the general perspective,
but with the difference that the point of perspective lies in infinite distance.
It is therefore often used to give the appearance of a globe viewed from outer
space, were one hemisphere can be seen as a whole. It is neither conformal nor
equal-area and the distortion increases near the edges.

``glon0/lat0[/horizon]/scale`` or ``Glon0/lat0[/horizon]/width``

``lon0/lat0`` specifies the projection center, the optional parameter ``horizon``
specifies the max distance from projection center (in degrees, <= 90, default 90)
"""
import pygmt

fig = pygmt.Figure()
fig.coast(projection="G10/52/4.5i", region="g", frame="g", land="gray")
fig.show()
