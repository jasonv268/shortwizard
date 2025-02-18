from pathlib import Path
from shortwizard.config import root_assets
from shortwizard.editor_utils.video.Video import Video
from shortwizard.editor_utils.img.Basique import default_has_mask


def get_emote(number) -> Video:
    return Video(globals()[f'_{number}']).set_basique(default_has_mask)


_1_Grinning_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '1_Grinning Face.mov')
_1 = _1_Grinning_Face
_2_Beaming_Face = Path(root_assets / 'video' / 'emotes' /
                       'pack1' / '2_Beaming Face.mov')
_2 = _2_Beaming_Face
_3_Face_With_Tears = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '3_Face With Tears.mov')
_3 = _3_Face_With_Tears
_4_Rolling_on_the_Floor = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '4_Rolling on the Floor.mov')
_4 = _4_Rolling_on_the_Floor
_5_Grinning_Face_With_Big_Eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '5_Grinning Face With Big Eyes.mov')
_5 = _5_Grinning_Face_With_Big_Eyes
_6_Grinning_Face_With_Smiling_Eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '6_Grinning Face With Smiling Eyes.mov')
_6 = _6_Grinning_Face_With_Smiling_Eyes
_7_Grinning_Face_With_Sweat = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '7_Grinning Face With Sweat.mov')
_7 = _7_Grinning_Face_With_Sweat
_8_Grinning_Squinting_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '8_Grinning Squinting Face.mov')
_8 = _8_Grinning_Squinting_Face
_9_Winking_Face = Path(root_assets / 'video' / 'emotes' /
                       'pack1' / '9_Winking Face.mov')
_9 = _9_Winking_Face
_10_Smiling_Face_Blushing = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '10_Smiling Face Blushing.mov')
_10 = _10_Smiling_Face_Blushing
_11_Face_Savoring_Food = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '11_Face Savoring Food.mov')
_11 = _11_Face_Savoring_Food
_12_Smiling_Face_With_Sunglasses = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '12_Smiling Face With Sunglasses.mov')
_12 = _12_Smiling_Face_With_Sunglasses
_13_Smiling_Face_With_Heart_Eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '13_Smiling Face With Heart-Eyes.mov')
_13 = _13_Smiling_Face_With_Heart_Eyes
_14_Face_Blowing_a_Kiss = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '14_Face Blowing a Kiss.mov')
_14 = _14_Face_Blowing_a_Kiss
_15_Kissing_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '15_Kissing Face.mov')
_15 = _15_Kissing_Face
_16_Kissing_Face_With_Smiling_Eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '16_Kissing Face With Smiling Eyes.mov')
_16 = _16_Kissing_Face_With_Smiling_Eyes
_17_Kissing_Face_With_Closed_Eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '17_Kissing Face With Closed Eyes.mov')
_17 = _17_Kissing_Face_With_Closed_Eyes
_18_Blushing_Closed_eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '18_Blushing Closed eyes.mov')
_18 = _18_Blushing_Closed_eyes
_19_Slightly_Smiling_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '19_Slightly Smiling Face.mov')
_19 = _19_Slightly_Smiling_Face
_20_Hugging_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '20_Hugging Face.mov')
_20 = _20_Hugging_Face
_21_Star_Struck = Path(root_assets / 'video' / 'emotes' /
                       'pack1' / '21_Star-Struck.mov')
_21 = _21_Star_Struck
_22_Thinking_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '22_Thinking Face.mov')
_22 = _22_Thinking_Face
_23_Face_With_Raised_Eyebrow = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '23_Face With Raised Eyebrow.mov')
_23 = _23_Face_With_Raised_Eyebrow
_24_Neutral_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '24_Neutral Face.mov')
_24 = _24_Neutral_Face
_25_Expressionless_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '25_Expressionless Face.mov')
_25 = _25_Expressionless_Face
_26_Face_Without_Mouth = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '26_Face Without Mouth.mov')
_26 = _26_Face_Without_Mouth
_27_Face_With_Rolling_Eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '27_Face With Rolling Eyes.mov')
_27 = _27_Face_With_Rolling_Eyes
_28_Smirking_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '28_Smirking Face.mov')
_28 = _28_Smirking_Face
_29_Persevering_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '29_Persevering Face.mov')
_29 = _29_Persevering_Face
_30_Sad_but_Relieved_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '30_Sad but Relieved Face.mov')
_30 = _30_Sad_but_Relieved_Face
_31_Face_With_Open_Mouth = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '31_Face With Open Mouth.mov')
_31 = _31_Face_With_Open_Mouth
_32_Zipper_Mouth_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '32_Zipper-Mouth Face.mov')
_32 = _32_Zipper_Mouth_Face
_33_Hushed_Face = Path(root_assets / 'video' / 'emotes' /
                       'pack1' / '33_Hushed Face.mov')
_33 = _33_Hushed_Face
_34_Sleepy_Face = Path(root_assets / 'video' / 'emotes' /
                       'pack1' / '34_Sleepy Face.mov')
_34 = _34_Sleepy_Face
_35_Tired_Face = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '35_Tired Face.mov')
_35 = _35_Tired_Face
_36_Sleeping_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '36_Sleeping Face.mov')
_36 = _36_Sleeping_Face
_37_Relieved_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '37_Relieved Face.mov')
_37 = _37_Relieved_Face
_38_Face_With_Tongue = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '38_Face With Tongue.mov')
_38 = _38_Face_With_Tongue
_39_Winking_Face_With_Tongue = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '39_Winking Face With Tongue.mov')
_39 = _39_Winking_Face_With_Tongue
_40_Squinting_Face_With_Tongue = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '40_Squinting Face With Tongue.mov')
_40 = _40_Squinting_Face_With_Tongue
_41_Drooling_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '41_Drooling Face.mov')
_41 = _41_Drooling_Face
_42_Unamused_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '42_Unamused Face.mov')
_42 = _42_Unamused_Face
_43_Downcast_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '43_Downcast Face.mov')
_43 = _43_Downcast_Face
_44_Pensive_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '44_Pensive Face.mov')
_44 = _44_Pensive_Face
_45_Confused_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '45_Confused Face.mov')
_45 = _45_Confused_Face
_46_Upside_Down_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '46_Upside-Down Face.mov')
_46 = _46_Upside_Down_Face
_47_Money_Mouth_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '47_Money-Mouth Face.mov')
_47 = _47_Money_Mouth_Face
_48_Astonished_Face = Path(root_assets / 'video' /
                           'emotes' / 'pack1' / '48_Astonished Face.mov')
_48 = _48_Astonished_Face
_49_Frowning_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '49_Frowning Face.mov')
_49 = _49_Frowning_Face
_50_Slightly_Frowning_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '50_Slightly Frowning Face.mov')
_50 = _50_Slightly_Frowning_Face
_51_Confounded_Face = Path(root_assets / 'video' /
                           'emotes' / 'pack1' / '51_Confounded Face.mov')
_51 = _51_Confounded_Face
_52_Disappointed_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '52_Disappointed Face.mov')
_52 = _52_Disappointed_Face
_53_Worried_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '53_Worried Face.mov')
_53 = _53_Worried_Face
_54_Face_With_Steam_From_Nose = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '54_Face With Steam From Nose.mov')
_54 = _54_Face_With_Steam_From_Nose
_55_Crying_Face = Path(root_assets / 'video' / 'emotes' /
                       'pack1' / '55_Crying Face.mov')
_55 = _55_Crying_Face
_56_Loudly_Crying_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '56_Loudly Crying Face.mov')
_56 = _56_Loudly_Crying_Face
_57_Frowning_Face_With_Open_Mouth = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '57_Frowning Face With Open Mouth.mov')
_57 = _57_Frowning_Face_With_Open_Mouth
_58_Anguished_Face = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '58_Anguished Face.mov')
_58 = _58_Anguished_Face
_59_Fearful_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '59_Fearful Face.mov')
_59 = _59_Fearful_Face
_60_Weary_Face = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '60_Weary Face.mov')
_60 = _60_Weary_Face
_61_Exploding_Head = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '61_Exploding Head.mov')
_61 = _61_Exploding_Head
_62_Grimacing_Face = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '62_Grimacing Face.mov')
_62 = _62_Grimacing_Face
_63_Anxious_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '63_Anxious Face.mov')
_63 = _63_Anxious_Face
_64_Face_Screaming_in_Fear = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '64_Face Screaming in Fear.mov')
_64 = _64_Face_Screaming_in_Fear
_65_Flushed_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '65_Flushed Face.mov')
_65 = _65_Flushed_Face
_66_Zany_Face = Path(root_assets / 'video' / 'emotes' /
                     'pack1' / '66_Zany Face.mov')
_66 = _66_Zany_Face
_67_Dizzy_Face = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '67_Dizzy Face.mov')
_67 = _67_Dizzy_Face
_68_Pouting_Face = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '68_Pouting Face.mov')
_68 = _68_Pouting_Face
_69_Angry_Face = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '69_Angry Face.mov')
_69 = _69_Angry_Face
_70_Face_With_Symbols_on_Mouth = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '70_Face With Symbols on Mouth.mov')
_70 = _70_Face_With_Symbols_on_Mouth
_71_Face_With_Medical_Mask = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '71_Face With Medical Mask.mov')
_71 = _71_Face_With_Medical_Mask
_72_Face_With_Thermometer = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '72_Face With Thermometer.mov')
_72 = _72_Face_With_Thermometer
_73_Face_With_Head_Bandage = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '73_Face With Head-Bandage.mov')
_73 = _73_Face_With_Head_Bandage
_74_Nauseated_Face = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '74_Nauseated Face.mov')
_74 = _74_Nauseated_Face
_75_Face_Vomiting = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '75_Face Vomiting.mov')
_75 = _75_Face_Vomiting
_76_Sneezing_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '76_Sneezing Face.mov')
_76 = _76_Sneezing_Face
_77_Smiling_Face_With_Halo = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '77_Smiling Face With Halo.mov')
_77 = _77_Smiling_Face_With_Halo
_78_Cowboy_Hat = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '78_Cowboy Hat.mov')
_78 = _78_Cowboy_Hat
_79_Clown_Face = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '79_Clown Face.mov')
_79 = _79_Clown_Face
_80_Lying_Face = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '80_Lying Face.mov')
_80 = _80_Lying_Face
_81_Shushing_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '81_Shushing Face.mov')
_81 = _81_Shushing_Face
_82_Face_With_Hand_Over_Mouth = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '82_Face With Hand Over Mouth.mov')
_82 = _82_Face_With_Hand_Over_Mouth
_83_Face_With_Monocle = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '83_Face With Monocle.mov')
_83 = _83_Face_With_Monocle
_84_Nerd_Face = Path(root_assets / 'video' / 'emotes' /
                     'pack1' / '84_Nerd Face.mov')
_84 = _84_Nerd_Face
_85_Hot_Face = Path(root_assets / 'video' / 'emotes' /
                    'pack1' / '85_Hot Face.mov')
_85 = _85_Hot_Face
_86_Partying_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '86_Partying Face.mov')
_86 = _86_Partying_Face
_87_Pleading_Face = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '87_Pleading Face.mov')
_87 = _87_Pleading_Face
_88_Woozy_Face = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '88_Woozy Face.mov')
_88 = _88_Woozy_Face
_89_Cold_Face = Path(root_assets / 'video' / 'emotes' /
                     'pack1' / '89_Cold Face.mov')
_89 = _89_Cold_Face
_90_Smiling_Face_With_Hearts = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '90_Smiling Face With Hearts.mov')
_90 = _90_Smiling_Face_With_Hearts
_91_Smiling_Face_With_Horns = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '91_Smiling Face With Horns.mov')
_91 = _91_Smiling_Face_With_Horns
_92_Angry_Face_With_Horns = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '92_Angry Face With Horns.mov')
_92 = _92_Angry_Face_With_Horns
_93_Grinning_Cat_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '93_Grinning Cat Face.mov')
_93 = _93_Grinning_Cat_Face
_94_Grinning_Cat_Face_With_Smiling_Eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '94_Grinning Cat Face With Smiling Eyes.mov')
_94 = _94_Grinning_Cat_Face_With_Smiling_Eyes
_95_Cat_Face_With_Tears_of_Joy = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '95_Cat Face With Tears of Joy.mov')
_95 = _95_Cat_Face_With_Tears_of_Joy
_96_Smiling_Cat_Face_With_Heart_Eyes = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '96_Smiling Cat Face With Heart-Eyes.mov')
_96 = _96_Smiling_Cat_Face_With_Heart_Eyes
_97_Cat_Face_With_Wry_Smile = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '97_Cat Face With Wry Smile.mov')
_97 = _97_Cat_Face_With_Wry_Smile
_98_Kissing_Cat_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '98_Kissing Cat Face.mov')
_98 = _98_Kissing_Cat_Face
_99_Weary_Cat_Face = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '99_Weary Cat Face.mov')
_99 = _99_Weary_Cat_Face
_100_Crying_Cat_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '100_Crying Cat Face.mov')
_100 = _100_Crying_Cat_Face
_101_Pouting_Cat_Face = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '101_Pouting Cat Face.mov')
_101 = _101_Pouting_Cat_Face
_102_See_No_Evil_Monkey = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '102_See-No-Evil Monkey.mov')
_102 = _102_See_No_Evil_Monkey
_103_Hear_No_Evil_Monkey = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '103_Hear-No-Evil Monkey.mov')
_103 = _103_Hear_No_Evil_Monkey
_104_Speak_No_Evil_Monkey = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '104_Speak-No-Evil Monkey.mov')
_104 = _104_Speak_No_Evil_Monkey
_105_Red_Heart = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '105_Red Heart.mov')
_105 = _105_Red_Heart
_106_Broken_Heart = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '106_Broken Heart.mov')
_106 = _106_Broken_Heart
_107_Revolving_Hearts = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '107_Revolving Hearts.mov')
_107 = _107_Revolving_Hearts
_108_Two_Hearts = Path(root_assets / 'video' / 'emotes' /
                       'pack1' / '108_Two Hearts.mov')
_108 = _108_Two_Hearts
_109_Flexed_Biceps = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '109_Flexed Biceps.mov')
_109 = _109_Flexed_Biceps
_110_Shaka_hand = Path(root_assets / 'video' / 'emotes' /
                       'pack1' / '110_Shaka hand.mov')
_110 = _110_Shaka_hand
_111_Waving_Hand = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '111_Waving Hand.mov')
_111 = _111_Waving_Hand
_112_OK_Hand = Path(root_assets / 'video' / 'emotes' /
                    'pack1' / '112_OK Hand.mov')
_112 = _112_OK_Hand
_113_Victory_Hand = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '113_Victory Hand.mov')
_113 = _113_Victory_Hand
_114_Crossed_Fingers = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '114_Crossed Fingers.mov')
_114 = _114_Crossed_Fingers
_115_Sign_of_the_Horns = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '115_Sign of the Horns.mov')
_115 = _115_Sign_of_the_Horns
_116_Love_You_Gesture = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '116_Love-You Gesture.mov')
_116 = _116_Love_You_Gesture
_117_Thumbs_Up = Path(root_assets / 'video' / 'emotes' /
                      'pack1' / '117_Thumbs Up.mov')
_117 = _117_Thumbs_Up
_118_Thumbs_Down = Path(root_assets / 'video' /
                        'emotes' / 'pack1' / '118_Thumbs Down.mov')
_118 = _118_Thumbs_Down
_119_Vulcan_Salute = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '119_Vulcan Salute.mov')
_119 = _119_Vulcan_Salute
_120_Clapping_Hands = Path(root_assets / 'video' /
                           'emotes' / 'pack1' / '120_Clapping Hands.mov')
_120 = _120_Clapping_Hands
_121_Folded_Hands = Path(root_assets / 'video' /
                         'emotes' / 'pack1' / '121_Folded Hands.mov')
_121 = _121_Folded_Hands
_122_Middle_Finger = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '122_Middle Finger.mov')
_122 = _122_Middle_Finger
_123_Backhand_Index_Pointing_Right = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '123_Backhand Index Pointing Right.mov')
_123 = _123_Backhand_Index_Pointing_Right
_124_Raising_Hands = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '124_Raising Hands.mov')
_124 = _124_Raising_Hands
_125_Eyes = Path(root_assets / 'video' / 'emotes' / 'pack1' / '125_Eyes.mov')
_125 = _125_Eyes
_126_Man_Shrugging = Path(root_assets / 'video' /
                          'emotes' / 'pack1' / '126_Man Shrugging.mov')
_126 = _126_Man_Shrugging
_127_Woman_Shrugging = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '127_Woman Shrugging.mov')
_127 = _127_Woman_Shrugging
_128_Man_Facepalming = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '128_Man Facepalming.mov')
_128 = _128_Man_Facepalming
_129_Woman_Facepalming = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '129_Woman Facepalming.mov')
_129 = _129_Woman_Facepalming
_130_Man_Gesturing_No = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '130_Man Gesturing No.mov')
_130 = _130_Man_Gesturing_No
_131_Woman_Gesturing_No = Path(
    root_assets / 'video' / 'emotes' / 'pack1' / '131_Woman Gesturing No.mov')
_131 = _131_Woman_Gesturing_No
_132_Fire = Path(root_assets / 'video' / 'emotes' / 'pack1' / '132_Fire.mov')
_132 = _132_Fire
