import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fftshift, fft2
from skimage.draw import polygon

def create_star_aperture(size, num_points=5, radius=80, center=None):
    if center is None:
        center = (size // 2, size // 2)
    
    img = np.zeros((size, size), dtype=np.float32)
    
    angles = np.linspace(0, 2 * np.pi, num_points * 2, endpoint=False)
    radii = np.array([radius, radius / 2] * num_points)
    
    x = center[0] + (radii * np.sin(angles)).astype(np.int32)
    y = center[1] + (radii * np.cos(angles)).astype(np.int32)
    
    rr, cc = polygon(x, y, img.shape)
    img[rr, cc] = 1.0  # Set star shape to white (1) on black background (0)
    
    return img

def compute_fourier_transform(image):
    f_transform = fft2(image)
    f_transform_shifted = fftshift(f_transform)
    magnitude_spectrum = np.abs(f_transform_shifted)**2  
    return magnitude_spectrum

size = 512  
star_aperture = create_star_aperture(size)

fourier_image = compute_fourier_transform(star_aperture)

fourier_image = np.log(fourier_image + 1)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(star_aperture, cmap='gray')
plt.title('Star Aperture')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(fourier_image, cmap='hot')  # Hot colormap for better visibility
plt.title('Fourier Transform (Diffraction Pattern)')
plt.axis('off')

plt.show()