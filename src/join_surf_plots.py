#!/opt/miniconda3/envs/fmri/bin/python3
import os
import string
from PIL import Image, ImageDraw, ImageFont

def join_surf_plots(r, figpaths):
    
    def caption_plots(i, figpath):
        """ Adds text to ech image"""
        img = Image.open(figpath)
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("ArialUnicode.ttf", 50)
        font_BOLD = ImageFont.truetype("ArialUnicode.ttf", 100)

        # draw.text((x, y),"Sample Text",(r,g,b))
        # Draw Lefts and right
        draw.text(((img.width/4)-25, img.height-525), "Left", (0,0,0), font=font)
        draw.text(((img.width/4)*3-70, img.height-525), "Right", (0,0,0), font=font)
        
        # Draw Legend based on i
        draw.text((50, img.height-100), f"({string.ascii_uppercase[i]})", (0,0,0), font=font)
        return img
    
    def vjoin_plots(figs):
        """Stacks images vertically"""
        img = Image.new('RGB', (figs[0].width, figs[0].height * len(figs)))
        for i, fig in enumerate(figs):
            img.paste(fig, (0, fig.height*i))
        return img

    figs = [caption_plots(i, fig) for i, fig in enumerate(figpaths)]

    pub_all = vjoin_plots(figs)
    outpath = f'results/figures/surf/pub_all_surfs_size{r}.png'
    pub_all.save(outpath)
    print(f'Plot saved to {outpath}')

    return None


if __name__ == '__main__':
    
    WORKDIR = os.path.join(os.path.dirname(__file__), '..')
    os.chdir(WORKDIR)

    for r in 2,3,4:
        figpaths = ['results/figures/surf/pub_avgCBF_thr10.png',
                    f'results/figures/surf/pub_avgISLA_cbf_size{r}_thr10.png',
                    f'results/figures/surf/pub_avgAhlgren_cbf_size{r}_thr10.png',
                    'results/figures/surf/pub_avgBASIL_cbf_thr10.png']

        join_surf_plots(r, figpaths)
