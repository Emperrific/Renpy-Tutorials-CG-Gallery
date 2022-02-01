screen gallery:
    tag menu

    add "black"

    $start = gallery_page * maxperpage
    $end = min(start + maxperpage - 1, len(gallery_items) - 1)

    #grid for images
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
            else:
                imagebutton idle gallery_items[i].thumb:
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5

        for i in range(end - start + 1, maxperpage):
            null

    #grid for info
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            hbox:
                spacing maxthumbx - 70
                xalign 0.5
                yalign 0.1
                $total = gallery_items[i].num_images()
                $partial = gallery_items[i].num_unlocked
                text gallery_items[i].name
                text "[partial]/[total]"

        for i in range(end - start + 1, maxperpage):
            null


    #previous/next buttons
    $ total_page = len(gallery_items) / maxperpage
    $ current_page = gallery_page + 1
    textbutton "Previous":
            xalign 0.1
            yalign 0.98
            if gallery_page > 0:
                action SetVariable("gallery_page", gallery_page - 1)
            else:
                action SetVariable("gallery_page", total_page - 1)
    textbutton "[current_page] / [total_page] page":
        action None
        xalign 0.4
        yalign 0.98
    textbutton "Next":
        xalign 0.9
        yalign 0.98
        if (gallery_page + 1) * maxperpage < len(gallery_items):
            action SetVariable("gallery_page", gallery_page + 1)
        else:
            action SetVariable("gallery_page", 0)
    #return button
    textbutton "Return":
        action Return()
        xalign 0.6
        yalign 0.98

screen gallery_closeup(images):
    if closeup_page < len(images) - 1:
        key ["game_menu", "K_RETURN","mouseup_1"] action SetVariable("closeup_page", closeup_page + 1)
    else:
        key ["game_menu", "K_RETURN","mouseup_1"] action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
    add images[closeup_page] at truecenter
