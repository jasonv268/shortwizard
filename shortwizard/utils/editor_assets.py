import moviepy.editor as mpe

def create_audio(path, max_duration: int):

    audio_clip = mpe.AudioFileClip(path)

    if audio_clip.duration > max_duration:
        audio_clip = audio_clip.subclip(0, max_duration)

    return audio_clip

def fade_in_out_audio(audio_clip, fadein_duration=2, fadeout_duration=2):
        # Appliquer un fondu en entrée
        audio_fadein = audio_clip.audio_fadein(fadein_duration)

        # Appliquer un fondu en sortie
        audio_fadeout = audio_fadein.audio_fadeout(fadeout_duration)

        return audio_fadeout


def crop_bg(bg_clip):
        h_original = bg_clip.h

        w_edit = bg_clip.w*1920 / h_original

        bg_clip = bg_clip.resize((w_edit, 1920)).on_color(
            size=(1080, 1920), color=(0, 0, 0))

        return bg_clip

def fade_in_out_bg(bg_clip):
    # Fondu en entrée (fade in)
    fondu_clip_in = bg_clip.subclip(0, 1)
    fondu_fade_in = fondu_clip_in.fadein(1)

    # Fondu en sortie (fade out)
    fondu_clip_out = bg_clip.subclip(
        bg_clip.duration - 1, bg_clip.duration)
    fondu_fade_out = fondu_clip_out.fadeout(1)

    # Composition du fondu d'entrée et de sortie avec la vidéo de fond
    bg_clip = mpe.concatenate_videoclips([
        fondu_fade_in,
        bg_clip.subclip(1, bg_clip.duration - 1),
        fondu_fade_out
    ])

    return bg_clip

def create_text(text, position, t1, t2, font_size, chars_per_line):

    def diviser_texte(texte, longueur_max):
        mots = texte.split(' ')
        parties = []
        partie_actuelle = ""

        for mot in mots:
            if len(partie_actuelle) + len(mot) + 1 <= longueur_max:  # Ajoute 1 pour l'espace
                if partie_actuelle:  # Ajoute un espace si nécessaire
                    partie_actuelle += " "
                partie_actuelle += mot
            else:
                parties.append(partie_actuelle)
                partie_actuelle = mot

        if partie_actuelle:  # Ajoute la dernière partie
            parties.append(partie_actuelle)

        return parties

    list = diviser_texte(text, chars_per_line)

    text_clip_list = []

    for index, t in enumerate(list):
        text_clip = mpe.TextClip(txt=t, fontsize=font_size, color='white',stroke_color='red',
                                 stroke_width=3,font='Purisa-Bold')

        text_clip = text_clip.set_position(
            (position[0], position[1]+index*font_size*2)).set_duration((t2-t1)-1).set_start(t1-1)

        text_fadein = text_clip.crossfadein(1)

        # Appliquer un fondu en sortie
        text_fadeout = text_fadein.crossfadeout(1)

        text_clip_list.append(text_fadeout)

    return text_clip_list





def create_text_display(text_list, position, audio_config):
        
        text_clip_list = []
    
        text_clip_list += create_text(text_list[0], position, audio_config[0], audio_config[1], 100, 15)


        for index, text in enumerate(text_list[1:]):
            text_clip_list+= create_text(text, position, audio_config[index+1], audio_config[index+2], 50, 30)
           
        return text_clip_list



def create_text_clip_list(text, position, t1, t2, font_size, chars_per_line):

    def diviser_texte(texte, longueur_max):
        mots = texte.split(' ')
        parties = []
        partie_actuelle = ""

        for mot in mots:
            if len(partie_actuelle) + len(mot) + 1 <= longueur_max:  # Ajoute 1 pour l'espace
                if partie_actuelle:  # Ajoute un espace si nécessaire
                    partie_actuelle += " "
                partie_actuelle += mot
            else:
                parties.append(partie_actuelle)
                partie_actuelle = mot

        if partie_actuelle:  # Ajoute la dernière partie
            parties.append(partie_actuelle)

        return parties

    list = diviser_texte(text, chars_per_line)

    text_clip_list = []

    for index, t in enumerate(list):
        text_clip = mpe.TextClip(txt=t, fontsize=font_size, color='white',stroke_color='red',
                                 stroke_width=3,font='Purisa-Bold')

        text_clip = text_clip.set_position(
            (position[0], position[1]+index*font_size*2)).set_duration((t2-t1)-1).set_start(t1-1)

        text_fadein = text_clip.crossfadein(1)

        # Appliquer un fondu en sortie
        text_fadeout = text_fadein.crossfadeout(1)

        text_clip_list.append(text_fadeout)

    return text_clip_list


def edit_anim(path,start_time, end_time):
    follow_clip = mpe.VideoFileClip(path)

    follow_anim = follow_clip.subclip(start_time, end_time)
    follow_anim = follow_anim.resize((640, 360))
    follow_anim = follow_anim.set_position(("center",200))
    follow_anim = follow_anim.fx(
        mpe.vfx.mask_color, color=(95, 206, 29), thr=100, s=100)
    follow_anim = follow_anim.fx(mpe.vfx.speedx, 1.5)
    follow_anim.set_opacity(0.8)

    return follow_anim