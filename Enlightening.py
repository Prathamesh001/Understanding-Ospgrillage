import ospgrillage as og
# create unit signs for variables of example
kilo = 1e3
milli = 1e-3
N = 1
m = 1
mm = milli * m
m2 = m ** 2
m3 = m ** 3
m4 = m ** 4
kN = kilo * N
MPa = N / ((mm) ** 2)
GPa = kilo * MPa

concrete = og.create_material(material = "concrete", code = "AS5100-2017", grade = "50MPa")
##I_beam central 3 long lines
I_beam_section = og.create_section(A=0.896*m2, J=0.133*m4, Iy=0.213*m4, Iz=0.259*m4, Ay=0.233*m2, Az=0.58*m2)
##
I_beam = og.create_member(section = I_beam_section, material = concrete)
##Edge beams extreme longi members
edge_beam_section = og.create_section(A=0.044625*m2,J=2.28e-3*m4, Iy=2.23e-1*m4,Iz=1.2e-3*m4, Ay=3.72e-2*m2, Az=3.72e-2*m2)
edge_beam = og.create_member(section = edge_beam_section, material = concrete)
##Edge slab
edge_slab_section = og.create_section(A=0.039375*m2,J=0.21e-3*m4, Iy=0.1e-3*m2,Iz=0.166e-3*m2,Ay=0.0328*m2, Az=0.0328*m2)
edge_slab = og.create_member(section = edge_slab_section, material = concrete)
##Slab transverse members
slab_section = og.create_section(A=0.04428*m2, J=2.6e-4*m4, Iy=1.1e-4*m4, Iz=2.42e-4*m4,Ay=3.69e-1*m2, Az=3.69e-1*m2, unit_width=True)
slab = og.create_member(section = slab_section, material = concrete)

example_bridge = og.create_grillage(bridge_name="My_bridge",
                                    long_dim=10,
                                    width=5,
                                    skew=21,
                                    num_long_grid=7,
                                    num_trans_grid=17,
                                    #edge_beam_dist=1,
                                    #mesh_type="Ortho"
                                    )

example_bridge.create_osp_model(pyfile=False)
og.opsv.plot_model(az_el=(-90, 0)) # using osp_vis
fig = og.plt.gcf()
og.plt.show()


##Set members
example_bridge.set_member(I_beam, member="interior_main_beam")
example_bridge.create_osp_model(pyfile=False)
og.opsv.plot_model(az_el=(-90, 0)) # using osp_vis
fig = og.plt.gcf()
og.plt.show()

example_bridge.set_member(edge_beam, member="edge_beam")
example_bridge.create_osp_model(pyfile=False)
og.opsv.plot_model(az_el=(-90, 0)) # using osp_vis
fig = og.plt.gcf()
og.plt.show()

example_bridge.set_member(edge_slab, member="start_edge")
example_bridge.create_osp_model(pyfile=False)
og.opsv.plot_model(az_el=(-90, 0)) # using osp_vis
fig = og.plt.gcf()
og.plt.show()


example_bridge.set_member(edge_slab, member="end_edge")
example_bridge.create_osp_model(pyfile=False)
og.opsv.plot_model(az_el=(-90, 0)) # using osp_vis
fig = og.plt.gcf()
og.plt.show()

example_bridge.set_member(slab, member="transverse_slab")
example_bridge.create_osp_model(pyfile=False)
og.opsv.plot_model(az_el=(-90, 0)) # using osp_vis
fig = og.plt.gcf()
og.plt.show()

example_bridge.set_member(I_beam, member="exterior_main_beam_1")
example_bridge.create_osp_model(pyfile=False)
og.opsv.plot_model(az_el=(-90, 0)) # using osp_vis
fig = og.plt.gcf()
og.plt.show()

example_bridge.set_member(I_beam, member="exterior_main_beam_2")

##Display plot
example_bridge.create_osp_model(pyfile=False)
og.opsv.plot_model(az_el=(-90, 0)) # using osp_vis
fig = og.plt.gcf()
og.plt.show()
