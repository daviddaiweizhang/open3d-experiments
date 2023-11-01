import open3d as o3d

bunny = o3d.data.BunnyMesh()
mesh = o3d.io.read_triangle_mesh(bunny.path)
mesh.compute_vertex_normals()
o3d.visualization.draw_geometries([mesh])
