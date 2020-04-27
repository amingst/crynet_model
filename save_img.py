import matplotlib.pyplot as plt

# TODO: Add Completed Message
def save_img(fig, path, img_name, class_label):
    full_path = path + class_label + '/' + img_name
    plt.savefig(full_path, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

    return None