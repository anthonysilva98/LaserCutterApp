//
//  MachineMenu.swift
//  LazerCut
//
//  Created by Anthony Silva on 6/29/20.
//  Copyright © 2020 Anthony Silva. All rights reserved.
//

import SwiftUI

struct MachineMenu: View {
    @State var MachineXstring = ""
    @State var MachineYstring = ""
    @State var MachineX = Int.self
    @State var MachineY = Int.self
    var body: some View {
        ZStack{
            Rectangle().edgesIgnoringSafeArea(.all).foregroundColor(.white)
            
        }
        
    }
}

struct MachineMenu_Previews: PreviewProvider {
    static var previews: some View {
        MachineMenu()
    }
}
