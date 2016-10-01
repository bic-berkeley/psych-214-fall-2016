#- Use slicing to remove outlier volume from rest volumes
off_volumes_fixed = off_volumes[..., 1:]
