function advancedMenu() {
    selection=$(whiptail --title "Advanced Menu" --fb --menu "Choose an option" 15 60 4 \
        "1" "Create a Progress Quiz" \
        "2" "Create a single Module" \
        "3" "Create a single version of a Module" 3>&1 1>&2 2>&3)
    case $selection in
        1)
            examNumber=$(whiptail --inputbox "What quiz would you like to create? This should be 1, 2, 3, 4, 5, or 6." 8 39 --title "Creating Progress Quiz" 3>&1 1>&2 2>&3)
            semester=$(whiptail --inputbox "What semester would you like printed at the bottom of the page?" 8 39 --title "Creating Progress Quiz" 3>&1 1>&2 2>&3)
            if (whiptail --inputbox "Creating Progress Quiz $examNumber for semester $semester. Is this correct?" 10 39 --title "Creating Progress Quiz"); then
                {
                    for ((i = 0 ; i <= 100 ; i+=5)); do
                        sleep 0.1
                        echo $i
                    done
                } | whiptail --gauge "Code is running..." 6 50 0
            fi
        ;;
        2)
            echo "Option 2"
            whiptail --title "Option 1" --msgbox "You chose option 2. Exit status $?" 8 45
        ;;
        3)
            echo "Option 3"
            whiptail --title "Option 1" --msgbox "You chose option 3. Exit status $?" 8 45
        ;;
    esac
}
advancedMenu
whiptail --title "Completed!" --msgbox "The quiz has finished running." 8 78
