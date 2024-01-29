import io

import imageio
from matplotlib import pyplot

with imageio.get_writer('pyplot_video_writer.mp4', fps=24) as writer:
    pyplot.figure()
    for i in range(100):
        pyplot.plot([x for x in range(i)], [x**2 for x in range(i)])
        buffer = io.BytesIO()  # in-memory byte buffer
        pyplot.savefig(buffer, format='png')
        buffer.seek(0)  # reset pointer to the start of the buffer
        image = imageio.v2.imread(buffer)
        writer.append_data(image)
        buffer.close()
