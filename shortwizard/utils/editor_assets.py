import moviepy.editor as mpe

from shortwizard.utils import Effect


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
    fondu_clip_in = bg_clip.subclip(0, 0.5)
    fondu_fade_in = fondu_clip_in.fadein(0.5)

    # Fondu en sortie (fade out)
    fondu_clip_out = bg_clip.subclip(
        bg_clip.duration - 0.5, bg_clip.duration)
    fondu_fade_out = fondu_clip_out.fadeout(0.5)

    # Composition du fondu d'entrée et de sortie avec la vidéo de fond
    bg_clip = mpe.concatenate_videoclips([
        fondu_fade_in,
        bg_clip.subclip(0.5, bg_clip.duration - 0.5),
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
        text_clip = mpe.TextClip(txt=t, fontsize=font_size, color='white', stroke_color='red',
                                 stroke_width=3, font='Purisa-Bold')

        text_clip = text_clip.set_position(
            (position[0], position[1]+index*font_size*2)).set_duration((t2-t1)-1).set_start(t1-1)

        text_fadein = text_clip.crossfadein(1)

        # Appliquer un fondu en sortie
        text_fadeout = text_fadein.crossfadeout(1)

        text_clip_list.append(text_fadeout)

    return text_clip_list


def create_text_display(text_list, position, audio_config):

    text_clip_list = []

    text_clip_list += create_text(text_list[0], position,
                                  audio_config[0], audio_config[1], 100, 15)

    for index, text in enumerate(text_list[1:]):
        text_clip_list += create_text(text, position,
                                      audio_config[index+1], audio_config[index+2], 50, 30)

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
        text_clip = mpe.TextClip(txt=t, fontsize=font_size, color='white', stroke_color='black',
                                 stroke_width=5, font='Tiktok-Bold')

        text_clip = text_clip.set_position(
            (position[0], position[1]+index*font_size*2)).set_duration((t2-t1)).set_start(t1-1)

        text_fadein = text_clip.crossfadein(0.5)

        # Appliquer un fondu en sortie
        text_fadeout = text_fadein.crossfadeout(0.5)

        text_clip_list.append(text_fadeout)

    return text_clip_list


def edit_anim(path, start_time, end_time):
    follow_clip = mpe.VideoFileClip(path)

    follow_anim = follow_clip.subclip(start_time, end_time)
    follow_anim = follow_anim.resize((640, 360))
    follow_anim = follow_anim.set_position(("center", 200))
    follow_anim = follow_anim.fx(
        mpe.vfx.mask_color, color=(95, 206, 29), thr=100, s=100)
    follow_anim = follow_anim.fx(mpe.vfx.speedx, 1.5)
    follow_anim.set_opacity(0.8)

    return follow_anim


def create_anim(path, start_time, end_time, position):
    anim = mpe.VideoFileClip(path)

    anim = anim.subclip(start_time, end_time)
    # anim = anim.resize((640, 360))
    anim = anim.set_position(position)
    anim = anim.fx(
        mpe.vfx.mask_color, color=(1, 255, 11), thr=100, s=100)
    anim = anim.fx(mpe.vfx.speedx, 1.5)
    anim.set_opacity(0.8)

    return anim


def remove_green_screen(clip, effect: Effect.VideoEffect):

    anim = clip.fx(
        mpe.vfx.mask_color, color=effect.get_mask_color(), thr=100, s=100)
    anim.set_opacity(0.8)
    anim = anim.resize((640, 360))
    anim = anim.set_position(effect.get_position())

    return anim



def create_effects(effects: list[Effect.Effect], start_time, tts_duration):

    audio_clip_list, video_clip_list = [], []

    for effect in effects:
        if isinstance(effect, Effect.AudioEffect):

            sound_effect = mpe.AudioFileClip(
                effect.get_effect_path())

            if effect.get_start_time() == "TTSEND":
                sound_effect = sound_effect.set_start(
                    start_time+tts_duration)

            else:
                sound_effect = sound_effect.set_start(
                    start_time+effect.get_start_time())

            sound_effect = sound_effect.set_duration(
                min(effect.get_duration(), sound_effect.duration))
            audio_clip_list.append(sound_effect)

        elif isinstance(effect, Effect.ImageEffect):

            image_effect = mpe.ImageClip(effect.get_effect_path(),effect.get_position())
            image_effect = image_effect.set_position(effect.get_position())

            if effect.get_start_time() == "TTSEND":
                image_effect = image_effect.set_start(
                    tts_duration+start_time)
            else:
                image_effect = image_effect.set_start(
                    effect.get_start_time()+start_time)

            image_effect: mpe.ImageClip = image_effect.set_duration(
                min(effect.get_duration(), sound_effect.duration))

            video_clip_list.append(image_effect)

        elif isinstance(effect, Effect.VideoEffect):

            video_effect = mpe.VideoFileClip(effect.get_effect_path())
            video_effect = remove_green_screen(video_effect, effect)

            if effect.get_start_time() == "TTSEND":
                video_effect = video_effect.set_start(
                    tts_duration+start_time)
            else:
                video_effect = video_effect.set_start(
                    effect.get_start_time()+start_time)

            video_effect: mpe.VideoFileClip = video_effect.set_duration(
               min(effect.get_duration(), video_effect.duration))

            video_clip_list.append(video_effect)

    return audio_clip_list, video_clip_list
