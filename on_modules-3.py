def vol_means(image_fname):
    img = nib.load(image_fname)
    data = img.get_data()
    means = []
    for i in range(data.shape[-1]):
        vol = data[..., i]
        means.append(np.mean(vol))
    return means
