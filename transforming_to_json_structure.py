import re
import json


def transform_structure(data):
    output = []
    chapter_index = 1

    for chapter_title, sections in data.items():
        # Extract readable title
        match = re.match(r"Chapter\s+([\d.]+)\s+(.*)", chapter_title)
        # chapter_code = match.group(1) if match else f"{chapter_index:02d}"
        readable_title = match.group(2).title() if match else chapter_title

        article = {
            "title": f"Chapter {str(chapter_index)} {readable_title}",
            "dir": f"chapter_{chapter_index}",
            "file": "",
            "sections": []
        }

        for i, section in enumerate(sections, 1):
            section_entry = {
                "title": f"§ {section['heading']}",
                "file": f"{chapter_index}.{i}",
                "section": []
            }
            article["sections"].append(section_entry)

        output.append(article)
        chapter_index += 1

    return output

results = {
  "Chapter 27.02 GENERAL PROVISIONS": [
    {
      "heading": "27.02.010 TITLE.",
      "id": "/us/ca/cities/san-mateo/code/27.02.010",
      "text": "This title shall be known and may be cited and referred to as the \"San Mateo City Zoning Code.\""
    },
    {
      "heading": "27.02.020 INTENT—PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.02.020",
      "text": "This title is adopted for the following purposes: (a) To promote the public health, safety, morals, comfort, and general welfare; (b) To conserve the values of property throughout the City and to protect the character and stability of residential, commercial and manufacturing areas, and to promote the orderly and beneficial development of such areas; (c) To provide adequate light, air, privacy, and convenience of access to property; (d) To lessen or avoid congestion in the public streets and highways; (e) To regulate and restrict the location and use of buildings, structures, and land for trade, industry, residence and other uses, and to regulate and restrict the intensity of such uses, and to establish building or setback lines; (f) To divide the entire City into districts of such number, shape, area, and of such different classes, according to the use of land and buildings, and the intensity of such use, as may be deemed best suited to carry out the purposes of this code; (g) To prohibit uses, buildings or structures incompatible with the character of such districts respectively; (h) To prevent additions to and alterations or remodeling of existing buildings or structures in such a way as to avoid the restrictions and limitations lawfully imposed hereunder; (i) To protect against fire, panic, explosion, noxious fumes, and other hazards, in the interest of public health, safety, comfort, and general welfare; (j) To provide for the elimination of incompatible and nonconforming uses of land, buildings, and structures which are adversely affecting the character and value of desirable development in each district; and (k) To define the powers and duties of the administrative officers and bodies as provided herein."
    },
    {
      "heading": "27.02.030 MINIMUM REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.030",
      "text": "The provisions of this title shall be held to be the minimum requirements for the promotion of public health, safety, morals and welfare."
    },
    {
      "heading": "27.02.040 RELATIONSHIP WITH OTHER LAWS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.040",
      "text": "Where the conditions imposed by any provision of this title upon the use of land or buildings or upon the bulk of buildings are either more restrictive or less restrictive than comparable conditions imposed by any other provision of this title, or any statute, ordinance, or regulation of any kind, the provisions which are more restrictive (or which impose higher standards or requirements) shall govern."
    },
    {
      "heading": "27.02.050 EFFECT ON EXISTING AGREEMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.050",
      "text": "This title is not intended to abrogate any easement, covenant or any other private agreement, provided that where the regulations of this title are more restrictive (or impose higher standards or requirements) than such easements, covenants or other private agreements, the requirements of this title shall govern."
    },
    {
      "heading": "27.02.060 Height Limitations and Exceptions.",
      "id": "/us/ca/cities/san-mateo/code/27.02.060",
      "text": "(a) No building, structure, or land shall hereafter be used or occupied, and no building or part thereof, or other structure, shall be erected, raised, moved, reconstructed, extended, enlarged or altered except in conformance with the regulations specified for the district in which it is located, except as described in subsection (b). (b) The following are exempt from maximum height limitations: (1) Pergolas, trellises, skylights, attached flagpoles, parapet walls, roof gardens, screens (or similar features necessary to screen roof top mechanical equipment as described in subsection (2)), and other similar features related to architectural design or style and that are accessory to the primary structure in function and appearance provided that they do not add floor area. (2) Roof top mechanical equipment such as cooling towers, elevators (including related equipment and bulkheads), solar collectors, and other mechanical equipment required for the property's use and size, provided that all roof top mechanical equipment shall be screened such that it is not visible from the adjacent public right-of-way(s). (3) Antennas mounted on a building or property by a public agency for public safety purposes. (4) Other accessory architectural features, subject to a Site Plan and Architectural Review (SPAR) planning application reviewed and approved by the Zoning Administrator. (c) For any application exempt under subsection (b), the Zoning Administrator may determine that additional review by the Planning Commission is required based on the size, shape, location, or impacts of the proposed feature in relation to the rest of the development. (d) For improvements or additions to existing nonconforming buildings, the maximum height and bulk regulations set forth elsewhere in this Title shall not apply to: (1) Improvements required for seismic retrofitting, Americans with Disability Act (ADA) accessibility, required life and safety upgrades, and historic preservation. (2) Mechanical upgrades, including but not limited to equipment upgrades, elevators (including related equipment and bulkheads), HVAC installation, and solar equipment installation; and any screening that may be necessary to screen the above, such that it is not visible from the public right-of-way."
    },
    {
      "heading": "27.02.070 TEMPORARY BUILDINGS ON A ZONING PLOT.",
      "id": "/us/ca/cities/san-mateo/code/27.02.070",
      "text": "A single, temporary structure to serve as an office for the sale or lease of buildings or facilities under construction may be permitted on the construction site if approved by the Zoning Administrator under an application for a site plan and architectural review as set forth in Section 27.08.030. Approval of such application shall include the following conditions: (a) The temporary structure and its facilities shall meet the health, safety and sanitation requirements for permanent structures. (b) The temporary structure shall be removed not later than 30 days after completion of all sales or leases of the buildings or facilities under construction, or 30 days after certification of occupancy of any structure or portion thereof, whichever occurs sooner; and in no event later than one year after approval of the temporary structure is final. (c) Plans for replacement and removal of the temporary structure must be approved by the building official. (d) Unless real estate sales are a permitted use in the district, a special use permit shall first be obtained by the applicant as set forth in Chapter 27.74 of this title, but in no event shall the temporary structure be used for transactions regarding any property off the site of the project where it is located. (e) Upon removal of the temporary structure, and if the district uses allow or the special use permit allows, the sales functions may occupy any structure in the development certified for occupancy for an additional period not to exceed that which may be set forth in the special use permit."
    },
    {
      "heading": "27.02.075 CONFORMANCE OF ZONING PLOTS WITH REGULATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.075",
      "text": "In the event that a zoning plot is divided or sold, all resulting zoning plots or parcels shall conform with all regulations of the zoning district in which the property is located. No use can be made of a resulting parcel(s) except in conformance with all regulations of the zoning district in which the property is located. There shall be no reduction in yards, open space, parking or other zoning requirements which causes or increases non-conformity."
    },
    {
      "heading": "27.02.080 REZONING OF PUBLIC AND SEMIPUBLIC AREAS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.080",
      "text": "No area used as a public park, recreation area, public school site, cemetery, or other public purpose shall be used for any private purpose until: (a) The public use of the area is abandoned; and (b) Appropriate zoning is authorized in accordance with provisions of this code."
    },
    {
      "heading": "27.02.090 PERFORMANCE STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.090",
      "text": "The performance standards for the M-1 manufacturing district as set forth in Chapter 27.56, pertaining to noise, smoke, odorous matter, vibration, toxic or noxious matter, glare or heat, fire and explosive hazards, shall also apply to all residence, commercial and executive districts."
    },
    {
      "heading": "27.02.100 EXISTING SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.02.100",
      "text": "Where a use is classified as a \"special use\" under this title, and exists as a permitted use at the date of the adoption of this chapter, it shall be considered a legal use, without further action of the Planning Commission or the City Council."
    },
    {
      "heading": "27.02.110 USES NOT SPECIFICALLY PERMITTED IN DISTRICTS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.110",
      "text": "When a use is not specifically listed in the sections devoted to \"uses permitted,\" it shall be assumed that such uses are prohibited unless it is determined by action of the City Council that the use is similar to and not more objectionable than uses listed."
    },
    {
      "heading": "27.02.120 INTERIM ZONING ORDINANCES/MORATORIA.",
      "id": "/us/ca/cities/san-mateo/code/27.02.120",
      "text": "Notwithstanding any other provisions of this code, the City Council may adopt an emergency ordinance to prohibit any uses of property that may be in conflict with a contemplated general plan, specific plan, building, sign, zoning regulation, and/or subdivision proposal that the City is studying or intends to study within a reasonable time. The ordinance may also suspend the operation of an existing ordinance for the period of the interim zoning ordinance/moratorium. After notice is given as provided in Section 27.08.050 for hearing before the City Council, the City Council may adopt regular or emergency ordinances to extend the interim zoning/moratoria ordinance for additional periods but not to exceed a total of 24 months inclusive of the initial period."
    },
    {
      "heading": "27.02.130 ZONING OF STREETS, ALLEYS, PUBLIC WAYS, AND RAILROAD RIGHTS-OF-WAY.",
      "id": "/us/ca/cities/san-mateo/code/27.02.130",
      "text": "All streets, alleys, public ways, and railroad rights-of-way, if not otherwise specifically designated, shall be deemed to be in the same zoning district as the property immediately abutting upon such alleys, streets, public ways, waterways, and railroad rights-of-way. Where the centerline of a street, alley, public way, waterway or railroad right-of-way serves as a district boundary, the zoning of such areas, unless otherwise specifically designated, shall be deemed to be the same as that of the abutting property up to such centerline."
    },
    {
      "heading": "27.02.140 Exceptions.",
      "id": "/us/ca/cities/san-mateo/code/27.02.140",
      "text": "The following uses in subsection (a) are exempted by this Title and allowed in any district. In addition, City projects that meet the criteria in subsection (b) below are also exempt: (a) Poles, towers, wires, cables, conduits, vaults, laterals, pipes, mains, valves or any other similar distributing and transmitting equipment for telephone or television communications, electric power, gas, water and sewer lines provided that the installation shall conform when applicable with Federal Communications Commission, State Public Utilities Commission, and Federal Aviation Agency rules and regulations, or any other authorities having jurisdiction and subject to other provisions of this code, City ordinances, rules and regulations. (b) The City project meets all of the following criteria: (1) It is accessory and/or ancillary to an existing or approved principal development or use; and (2) It is fully or partially funded by the City; and (3) The City has determined that the project is exempt from the provisions of the California Environmental Quality Act (CEQA)."
    },
    {
      "heading": "27.02.150 PREZONING OF UNINCORPORATED AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.02.150",
      "text": "Any unincorporated territory adjoining the City may be prezoned for the purpose of determining the classification that will apply to such property in the event of subsequent annexation to the City. The method of accomplishing such prezoning shall be as provided herein for the classifying or reclassifying of property within the City. The classification established by such prezoning action shall become effective at such time as the annexation becomes effective."
    },
    {
      "heading": "27.02.160 DENSITY TRANSFER.",
      "id": "/us/ca/cities/san-mateo/code/27.02.160",
      "text": "Transfer or allocation of density from one building site to another within the same planning or specific plan area may be permitted if both sites are under the ownership of the same person at the time of the transfer or allocation, or in the case of a specific plan, at the time of approval. Any such density transfer or allocation must be processed according to the procedures established for either special permits or planned development permits, provided that if the transfer or allocation is authorized by an approved specific plan, no further approval shall be required."
    },
    {
      "heading": "27.02.170 Consistency with General Plan.",
      "id": "/us/ca/cities/san-mateo/code/27.02.170",
      "text": "In their review of planning applications, each approval body involved shall consider whether the planning application is in conformance with the San Mateo City General Plan."
    },
    {
      "heading": "27.02.175 CONFORMITY WITH THE GENERAL PLAN—ACTIONS OF OTHER GOVERNMENT ENTITIES—PLANNING AGENCY.",
      "id": "/us/ca/cities/san-mateo/code/27.02.175",
      "text": "(a) The City Council and the Planning Commission in combination are designated as the planning agency to review and act upon matters designated in Government Code Section 65402(b) and (c) concerning the conformity of proposed actions of the County of San Mateo and local districts with the provisions of the City of San Mateo General Plan. The Planning Commission shall first consider such proposed actions and shall determine whether the proposed actions are or are not in conformance with the General Plan. The Commission decision shall be final, unless and until modified by the City Council. Upon the request of any Councilmember the City Council may thereafter consider the proposed actions and shall determine whether the proposed actions are or are not in conformance with the General Plan. The Council decision, if finding nonconformance, may specify conditions for the proposed action which would establish conformance. In the event that the Council determines that inadequate time is available to allow Planning Commission review to be completed, the Council may itself directly review the proposed actions and, absent Council concurrence, no further Planning Commission review shall occur. (b) The City Council is designated as the planning agency to review and take action upon matters designated in Government Code Section 65402(a) for the City of San Mateo and Section 65402(c) for the Redevelopment Agency of the City of San Mateo."
    },
    {
      "heading": "27.02.180 Relocation Assistance/Allowance.",
      "id": "/us/ca/cities/san-mateo/code/27.02.180",
      "text": "In the event of demolition of existing residential dwelling units and/or conversion causing relocation, a list of the head of household of each unit to be demolished or converted shall be provided to the Planning Division in order to determine that a planning application is complete. Relocation assistance shall be provided by a planning applicant to each household prior to any notice of relocation as follows: (a) A list of available comparable housing within San Mateo County; and (b) A relocation allowance in cash or check equivalent to three times the current monthly United States Department of Housing and Urban Development (HUD) Fair Market Rent for a dwelling unit of comparable size and type to the dwelling or room from which the displacement occurs; and (c) A payment not to exceed one thousand dollars ($1,000.00) for actual moving costs and related expenses incurred by the tenant household and substantiated by reasonably probative documentation; and (d) Other reasonable assistance and allowance, as determined by the final approval body in a condition of approval."
    },
    {
      "heading": "27.02.185 MULTIPLE USE SERVICE STATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.185",
      "text": "Except as specifically provided in this title, no zoning plot used as a service station may be the site of any other use at the same time."
    },
    {
      "heading": "27.02.190 HANDICAPPED ACCESS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.190",
      "text": "The Handicapped Access Regulations of the State as prepared by the Office of State Architect shall be followed wherever they are applicable."
    },
    {
      "heading": "27.02.200 MITIGATION OF ADVERSE IMPACT ON THE ENVIRONMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.02.200",
      "text": "In mitigating or avoiding significant adverse impact of a project on the environment the authority of the City shall not be less than its full scope of authority in the law for all other purposes."
    },
    {
      "heading": "27.02.210 VIOLATIONS OF PLANNING APPLICATION CONDITIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.210",
      "text": "It is unlawful for any person, firm, or corporation to violate conditions imposed on any land use permit granted pursuant to this title."
    },
    {
      "heading": "27.02.215 COMMUNITY RELATIONS COMMISSION—REVIEW OF VIOLATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.02.215",
      "text": "Notwithstanding any other provision of this Code, the Zoning Administrator may request the Community Relations Commission to order the abatement of violations of this title as provided in Chapter 7.16."
    },
    {
      "heading": "27.02.220 Consistency With Measure T, General Plan Ballot Measure (November 2024 Election).",
      "id": "/us/ca/cities/san-mateo/code/27.02.220",
      "text": "The provisions of Ordinance No. 2024-10, approved by the voters on November 5, 2024, as Measure T, and effective on December 19, 2024, allows for the full implementation of the Land Use Element in General Plan 2040. In case of conflict or inconsistency between Title 27 of the Municipal Code (Zoning Code) and the General Plan 2040, the uses, densities, intensities and heights specified in Table LU-1 (Land Use Designations) in the Land Use Element and associated with the Land Use Map shall control."
    }
  ],
  "Chapter 27.04 DEFINITIONS": [
    {
      "heading": "27.04.005 DEFINITIONS GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.005",
      "text": "In the construction of this title, the definitions contained in this chapter shall be observed and applied, except when the context clearly indicates otherwise."
    },
    {
      "heading": "27.04.008 ABUT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.008",
      "text": "To \"abut\" means that two or more zoning plots or districts share a lot line or zoning boundary in common. Plots in different zoning districts abut if more than one point of one plot is across the street from more than one point of another plot, and the zoning boundary is located in the middle of the street. Where two zoning plots or districts meet at a point but do not share a line in common, the two do not abut for zoning purposes. "
    },
    {
      "heading": "27.04.010 ACCESSORY BUILDING OR USE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.010",
      "text": "(a) An \"accessory building or use\" is one which: (1) Is subordinate to and serves a principal building or principle use; and (2) Is subordinate in area, extent or purpose to the principal building or principal use served; and (3) Contributes to the comfort, convenience or necessity of occupants of the principal building or principal use served; and (4) Is located on the same zoning lot as the principal building or principal use served except where accessory off-street parking facilities are permitted to locate off-site. (b) An \"accessory use\" includes, but is not limited to, the following: (1) A children's playhouse, garden house, private greenhouse, and lath house; (2) A garage, carport, shed, or building for domestic storage; (3) Incinerators incidental to residential use; (4) Stables, private; (5) Storage of merchandise normally carried in stock on the same lot with any retail service or business use; (6) Storage of goods used in or produced by manufacturing activities, on the same lot or parcel of ground with such activities; (7) Off-street motor vehicle parking areas, and loading and unloading facilities; (8) Public utility facilities: telephone, electric, gas, water and sewer lines, their supports and incidental equipment; (9) Multi-family recycling collection areas which conform to Section 27.86.030."
    },
    {
      "heading": "27.04.015 AGRICULTURE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.015",
      "text": "\"Agriculture\" means the tilling of soil, horticulture, floriculture, viticulture, raising crops, livestock, farming, dairying, animal husbandry, including all uses customarily accessory and incidental thereto; but excluding slaughterhouses, fertilizer works, bone yards, commercial feeding of garbage or offal to swine or other animals, or plants for the reduction of animal matter."
    },
    {
      "heading": "27.04.020 ALLEY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.020",
      "text": "\"Alley\" means a public way which affords only a secondary vehicular means of access to abutting property."
    },
    {
      "heading": "27.04.021 ALTERNATIVE FINANCIAL SERVICE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.021",
      "text": "\"Alternative financial service\" means a use, other than a State or Federally chartered bank, credit union, mortgage lender, savings and loan association, or industrial loan company, that offers deferred deposit transaction services or check cashing services and loans for payment of a percentage fee. The term \"alternative financial service\" includes, but is not limited to, deferred deposit transaction (payday loan) businesses that make loans upon assignment of wages received, check cashing businesses that charge a percentage fee for cashing a check or negotiable instrument, and motor vehicle title lenders who offer a short-term loan secured by the title to a motor vehicle. Non-profit financial institutions are not encompassed by the term \"alternative financial service.\" The term \"alternative financial service\" does not include retail sellers engaged primarily in the business of selling consumer goods to retail buyers and that cash checks for a minimum fee, not exceeding five percent, as a service to its customers that is incidental to its main purpose or business."
    },
    {
      "heading": "27.04.022 ANCILLARY USES AND STRUCTURES.",
      "id": "/us/ca/cities/san-mateo/code/27.04.022",
      "text": "\"Ancillary uses\" means developments in an adopted specific plan area, which are complementary to, but subordinate in height, bulk, volume and/or use to the principal development."
    },
    {
      "heading": "27.04.025 ANIMAL HOSPITAL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.025",
      "text": "\"Animal hospital\" means any buildings or portion thereof designed or used for the care, observation or treatment of cats, dogs or other household pets."
    },
    {
      "heading": "27.04.030 APARTMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.030",
      "text": "\"Apartment\" means a room or suite of rooms in a multiple family structure, which is arranged, designed or used as a single housekeeping unit and which includes cooking facilities."
    },
    {
      "heading": "27.04.033 ATRIUM.",
      "id": "/us/ca/cities/san-mateo/code/27.04.033",
      "text": "\"Atrium\" means an area within the building perimeter open to the sky, and used as a common area by employees, residents, or visitors of the development."
    },
    {
      "heading": "27.04.035 AUTOMOBILE SALES LOT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.035",
      "text": "\"Automobile sales lot\" means premises on which new or used passenger automobiles, trailers or trucks in operating condition are displayed in the open for sale or trade, and where no repair or service work is done."
    },
    {
      "heading": "27.04.040 AUTOMOBILE SERVICE STATION.",
      "id": "/us/ca/cities/san-mateo/code/27.04.040",
      "text": "\"Automobile service station\" means: (1) Premises devoted to the retail sale of motor vehicle fuel, lubricating oils, and similar products; (2) Premises providing services for lubrication, car washing, polishing, undersealing, minor motor tuneup and repair, ignition system repair and front end and wheel alignment, including minor work incidental to the foregoing where cutting and fitting machinery is employed; (3) Premises devoted to the retail sale and installation of batteries, tires, windshield wipers, spark plugs, headlights, tail and backup lights, mufflers, shock absorbers, brakes, seat covers and similar accessories, including minor work incidental to the foregoing where cutting and fitting machinery is employed; (4) The following is excluded and not permitted: engine replacement, major repair, including, but not limited to, framework and body repair work; the repair and installation of clutch, transmission and differentials, and further excluding any other work where cutting and fitting machinery is employed, except that cutting and fitting machinery may be used for that work which is specifically or incidentally authorized under subsections (2) and (3) of this section."
    },
    {
      "heading": "27.04.045 AWNING.",
      "id": "/us/ca/cities/san-mateo/code/27.04.045",
      "text": "\"Awning\" means a rooflike cover, temporary in nature, which projects from the wall of a building or overhangs the public way."
    },
    {
      "heading": "27.04.050 BALCONY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.050",
      "text": "\"Balcony\" means an elevated platform, enclosed by a parapet or a railing, projecting from an exterior wall of a building."
    },
    {
      "heading": "27.04.055 BASEMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.055",
      "text": "\"Basement\" is that portion of a building between floor and ceiling which is partly below and partly above grade. A basement is counted as a floor (story) of a building when more than one-half the area of outermost walls of the story is above finished or pre-existing grade (whichever is lower) and if the surface of the finished floor level above is more than four feet above average grade for more than 50% of the total perimeter or more than 12 feet above grade at any point."
    },
    {
      "heading": "27.04.056 BED AND BREAKFAST INN.",
      "id": "/us/ca/cities/san-mateo/code/27.04.056",
      "text": "\"Bed and breakfast inn\" means any structure in which guests are lodged on an overnight basis for compensation, in accordance with provisions of Section 27.16.070."
    },
    {
      "heading": "27.04.057 BEDROOM.",
      "id": "/us/ca/cities/san-mateo/code/27.04.057",
      "text": "\"Bedroom\" means an enclosed habitable space in a structure which: (1) is designed primarily for sleeping; (2) meets the room dimension requirements of the most recent edition of the Building Code, as shall have been adopted by the City Council; and (3) contains one or more windows. A room having the potential of being a bedroom shall be considered a bedroom for density and parking calculation purposes."
    },
    {
      "heading": "27.04.058 BICYCLE PARKING FACILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.058",
      "text": "\"Bicycle parking facility\" means a space exclusively for the storage of bicycles."
    },
    {
      "heading": "27.04.060 BLOCK.",
      "id": "/us/ca/cities/san-mateo/code/27.04.060",
      "text": "\"Block\" means a tract of land, as designated upon a subdivision map, bounded partially or wholly by streets, public parks, cemeteries, railroad rights-of-way, bulkhead lines, or shorelines of waterways of municipal boundary lines."
    },
    {
      "heading": "27.04.061 BLOCK CORNER.",
      "id": "/us/ca/cities/san-mateo/code/27.04.061",
      "text": "\"Block corner\" means a parcel which is a portion of a block that has a minimum of 50 feet of frontage on each of two or more intersecting public streets."
    },
    {
      "heading": "27.04.062 BLOCK FACE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.062",
      "text": "\"Block face\" means the frontage on the same side of the street and within the same block between intersecting streets."
    },
    {
      "heading": "27.04.065 BOARDING HOUSE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.065",
      "text": "\"Boarding house\" means a building where lodging and meals are provided for compensation for residents not functioning as a common household."
    },
    {
      "heading": "27.04.070 BUILDABLE AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.04.070",
      "text": "\"Buildable area\" means the space remaining on a zoning plot within which a building may be erected after the minimum required yard requirements of this title have been satisfied. "
    },
    {
      "heading": "27.04.075 BUILDING.",
      "id": "/us/ca/cities/san-mateo/code/27.04.075",
      "text": "\"Building\" means any structure with substantial walls and roof securely affixed to the land and entirely separated on all sides from any other structure by space or by walls in which there are no communicating doors, windows or opening, and which is designed or intended for the shelter, enclosure or protection of persons, animals, chattels or property of any kind. Any structure with interior areas not normally accessible for human use, such as gas holders, oil tanks, water tanks, grain elevators, coal bunkers, oil cracking towers, and other similar structures are not considered as buildings. (a) \"Completely enclosed building\" means a building separated on all sides from the adjacent open space, or from other buildings or other structures, by a permanent roof and by exterior walls or party walls, pierced only by windows and normal entrance or exit doors. (b) \"Detached building\" means a building separated by at least four feet of space open to the sky from any other building on the same zoning plot. (c) \"Existing building\" means a building erected prior to the effective date of the ordinance codified in this title, or one for which a legal building permit has been issued. (d) \"Principal building\" means a building in which is conducted the principal use of the lot on which it is situated. (e) \"Public building\" means a building principally occupied by the Federal, State, County or City government, or any political subdivision agency, or instrumentality thereof. (f) \"Temporary building\" means a building not permanently attached to the ground by fixed foundation, piers or substructure."
    },
    {
      "heading": "27.04.080 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.080",
      "text": "\"Building height\" means the vertical distance, measured from existing grade at any point along the perimeter of a building, to the highest plate line of the structure directly above that point, regardless of whether that point is on the same plane as the building where it touches the ground. Different setback requirements as a result of different building heights shall be applied to different portions of the building. Setback requirements determined by building height may utilize the height of an intermediate plate height of the building plane that touches the ground where the building above that intermediate plate height is set back a distance equal to 25% of the width of the structure at that point from the building plane that meets the ground, as illustrated in the following figure: "
    },
    {
      "heading": "27.04.085 BUILDING SETBACK LINE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.085",
      "text": "\"Building setback line\" means a line parallel to the front property line and rising vertically from the ground at a distance regulated by the front yard requirements set up in this title."
    },
    {
      "heading": "27.04.090 BULK.",
      "id": "/us/ca/cities/san-mateo/code/27.04.090",
      "text": "\"Bulk\" is the term used to describe the size and mutual relationships of buildings and other structures, as to size; height; coverage; shape; location of exterior walls in relation to lot lines, to the centerlines of the streets, to other walks of the same building, and to other buildings or structures; and to all open spaces relating to the building or structure."
    },
    {
      "heading": "27.04.095 BUSINESS.",
      "id": "/us/ca/cities/san-mateo/code/27.04.095",
      "text": "\"Business\" means any occupation, employment or enterprise wherein merchandise is exhibited or sold, or which occupies time, attention, labor and materials, or where services are offered for compensation."
    },
    {
      "heading": "27.04.100 BUS TERMINAL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.100",
      "text": "\"Bus terminal\" means a building or structure used for the storage or layover of passenger buses or motor coaches, including waiting rooms, rest rooms, and other facilities for passenger convenience."
    },
    {
      "heading": "27.04.105 CAR WASH.",
      "id": "/us/ca/cities/san-mateo/code/27.04.105",
      "text": "\"Car wash\" means an automated or nonautomated facility for and a process involving the washing and/or cleaning of motor vehicles, which may include drying facilities. To be designated a car wash, the use must constitute a major or principal use of the premises, rather than a casual or occasional use performed as an accommodation or convenience to customers."
    },
    {
      "heading": "27.04.107 CEMETERY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.107",
      "text": "\"Cemetery\" means a place for the internment and placement of human remains. A cemetery includes, but is not limited to, both below ground and aboveground graves, monuments, and other accessory uses."
    },
    {
      "heading": "27.04.110 CITY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.110",
      "text": "\"City\" means the City of San Mateo, California."
    },
    {
      "heading": "27.04.115 CITY COUNCIL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.115",
      "text": "\"City Council\" means the City Council of the City of San Mateo, California."
    },
    {
      "heading": "27.04.120 CLINIC—MEDICAL HEALTH CENTER.",
      "id": "/us/ca/cities/san-mateo/code/27.04.120",
      "text": "\"Clinic\" or \"medical health center\" means an establishment where patients are admitted for study and treatment by two or more licensed physicians and their professional associates, practicing medicine together."
    },
    {
      "heading": "27.04.125 CLUB OR LODGE, PRIVATE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.125",
      "text": "\"Private club\" or \"private lodge\" means a nonprofit association of persons, who are members, which owns, hires or leases a building, or portion thereof, the use of such premises being restricted to enrolled members and their guests."
    },
    {
      "heading": "27.04.127 COLUMBARIUM.",
      "id": "/us/ca/cities/san-mateo/code/27.04.127",
      "text": "\"Columbarium\" means an aboveground grave and structure made of vaults lined with recesses for cinerary urns."
    },
    {
      "heading": "27.04.130 COMMUNITY CARE FACILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.130",
      "text": "A \"community care facility\" means any place or building which is maintained and operated to provide 24-hour non-medical residential care, or day care services for children, adults, or both, limited to the following: (a) Residential Care Facility. A residential care facility means a family home, group care facility, residential care facility for the elderly, foster home, alcohol and/or drug recovery facility, intermediate care facility or similar facility, for 24-hour non-medical care of persons in need of personal services, supervision, or assistance essential for sustaining the activities of daily living or for the protection of the individual; (b) Day Care Center. A day care facility means any facility which provides non-medical care to persons in need of personal services, supervision, or assistance essential for sustaining the activities of daily living or for the protection of the individual on less than a 24-hour basis; (c) Family Day Care Home. A family day care home means a facility which provides care, protection, and supervision of no more than 14 children in the caregiver's own home, for periods of less than 24 hours per day, while the parents or guardians are away."
    },
    {
      "heading": "27.04.132 COMPACT CAR.",
      "id": "/us/ca/cities/san-mateo/code/27.04.132",
      "text": "\"Compact car\" means a passenger automobile not more than 16.17 feet long or 5.98 feet wide, or with a wheel base of 111 inches or less."
    },
    {
      "heading": "27.04.133 COOKING FACILITY/KITCHEN.",
      "id": "/us/ca/cities/san-mateo/code/27.04.133",
      "text": "\"Cooking facility/kitchen\" means a room or portion thereof designated and/or customarily used as a place for the preparation and sanitation of food and containing a sink, stove, refrigerator, oven, microwave, freezer, or any other customarily used appliance or fixture for the preparation and sanitation of food as determined by the Zoning Administrator. A \"cooking facility/kitchen\" does not include a \"wetbar\" or \"efficiency food preparation area.\""
    },
    {
      "heading": "27.04.135 CORRIDOR, OUTSIDE PUBLIC.",
      "id": "/us/ca/cities/san-mateo/code/27.04.135",
      "text": "\"Outside public corridor\" means a passageway, bounded by a parapet wall or railing, projecting from an exterior wall of a building and usually open to the sky except for overhanging roof eaves, and open to general or common use by more than one tenant or occupancy."
    },
    {
      "heading": "27.04.137 COVERED COURT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.137",
      "text": "A covered court means a common area within the building perimeter which is open from floor to ceiling, but which has a translucent roof or clerestory."
    },
    {
      "heading": "27.04.140 CURB LEVEL. [Repealed]",
      "id": "/us/ca/cities/san-mateo/code/27.04.140",
      "text": "Repealed."
    },
    {
      "heading": "27.04.143 DAYLIGHT PLANE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.143",
      "text": "\"Daylight plane\" means an inclined plane, beginning at a stated height above grade and extending into the site at a stated upward angle to the horizontal, which may limit the height or horizontal extent of structures at any specific point on the site where the daylight plane is more restrictive than the height limit or the minimum yard applicable at such point on the site."
    },
    {
      "heading": "27.04.144 DEN.",
      "id": "/us/ca/cities/san-mateo/code/27.04.144",
      "text": "\"Den\" means a habitable space in a structure meeting the room dimension requirements of the most recent edition of the Building Code, as shall have been adopted by the City Council, with one completely open side that is directly accessible to a kitchen, living room or dining room. Loft areas will be considered as dens if the above criteria are met, except that half-walls will not count as required wall openings. The term den includes, but is not limited to, types of rooms such as libraries, studies, sitting rooms, and sewing rooms."
    },
    {
      "heading": "27.04.145 DENSITY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.145",
      "text": "\"Density\" means the intensity of use expressed as unit density. (a) Unit density shall be based on the minimum lot area standards as designated in the zoning code. (b) The density range descriptions for each district shall be as follows:"
    },
    {
      "heading": "27.04.147 DEVELOPMENT REVIEW BOARD.",
      "id": "/us/ca/cities/san-mateo/code/27.04.147",
      "text": "The Development Review Board or Board means the staff level review board composed of representatives from the Building and Planning Divisions of the Department of Community Development, Department of Public Works, Fire Department, Police Department, and Department of Parks and Recreation."
    },
    {
      "heading": "27.04.150 DIRECTOR OF COMMUNITY DEVELOPMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.150",
      "text": "\"Director of Community Development\" means the Director of the Department of Community Development (Planning, Building, Housing, and Economic Development) of the City of San Mateo, California."
    },
    {
      "heading": "27.04.155 DISTRICT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.155",
      "text": "\"District\" means a section or part of the incorporated portion of the City for which the use regulations are uniform, as set forth herein."
    },
    {
      "heading": "27.04.156 DORMER.",
      "id": "/us/ca/cities/san-mateo/code/27.04.156",
      "text": "\"Dormer\" means a projecting window structure, set upright in a sloping roof."
    },
    {
      "heading": "27.04.160 DRIVE-IN ESTABLISHMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.160",
      "text": "\"Drive-in establishment\" means an establishment which accommodates the patrons' motor vehicles from which the occupants may watch, purchase or receive goods or services."
    },
    {
      "heading": "27.04.165 DWELLING.",
      "id": "/us/ca/cities/san-mateo/code/27.04.165",
      "text": "\"Dwelling\" means a building or portion thereof, designed or used exclusively for residential occupancy, including a one-family dwelling unit, an accessory dwelling unit, a junior accessory unit, a two-family dwelling unit, and a multiple-family dwelling unit but does not include a hotel, motel, boarding or lodging houses or other lodging facilities, or a vessel or boat, or a house trailer. (a) \"Accessory dwelling unit\" means an attached or detached residential dwelling unit which provides complete independent living facilities for one or more persons, is accessory to the primary single-family residential dwelling unit, and includes permanent provisions for living, sleeping, eating, cooking facilities and sanitation on the same parcel as the primary residential dwelling unit. (b) \"Bachelor, efficiency or studio unit\" means a dwelling unit consisting of one principal room used for living and sleeping purposes, plus cooking facilities, a bathroom, and closets. (c) \"Junior accessory dwelling unit\" means an additional, independent living unit constructed within the walls of a proposed or legally existing single-family residence, including attached garages. (d) \"Multiple-family dwelling\" means a building or portion thereof, designed or altered for occupancy by three or more families living independently of each other. (e) \"One-family dwelling\" means a building containing one cooking facility only and designed exclusively for use and occupancy by one family, including the provision of interior access to all bedrooms, and may include a junior accessory dwelling unit within the principal dwelling. (f) \"Two-family dwelling\" means a building(s) designed or altered to provide attached (duplex) or detached dwelling units for occupancy by two families living independently of each other."
    },
    {
      "heading": "27.04.170 DWELLING UNIT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.170",
      "text": "\"Dwelling unit\" means one or more rooms in a residential structure which are arranged or designed for use by one family, plus not more than two paying guests, which includes provisions for living, sleeping, eating, cooking and sanitation, and if located on multiple levels/stories, the unit provides interior connections from a common living area (including the living room, family room, dining room, kitchen, and other common living areas as determined by the Zoning Administrator). In addition, a \"primary residential dwelling unit\" means a building or separate portion thereof designated and/or customarily used as a residence by not more than one family and situated on a parcel or lot on which no other primary dwelling is located. The primary residential dwelling unit shall be larger, in terms of floor area, than any other residential structure situated on the same parcel or lot."
    },
    {
      "heading": "27.04.172 EFFICIENCY FOOD PREPARATION AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.04.172",
      "text": "\"Efficiency food preparation area\" means a small food preparation area for a junior accessory dwelling unit which includes sink dimensions with a maximum width of 16 inches and length of 16 inches, waste line diameter of 1.5 inches; food preparation with appliances that do not require electrical service greater than 120 volts, or natural or propane gas; a food preparation counter and storage cabinets which do not exceed six feet in length."
    },
    {
      "heading": "27.04.175 ELEEMOSYNARY USE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.175",
      "text": "\"Eleemosynary use\" means a use exclusively devoted to and supported by charity."
    },
    {
      "heading": "27.04.177 EMERGENCY SHELTER.",
      "id": "/us/ca/cities/san-mateo/code/27.04.177",
      "text": "\"Emergency shelter\" means overnight emergency housing, typically operated by a governmental or nonprofit agency, which is the principal shelter of the inhabitant for a temporary, emergency period. An \"emergency shelter\" is defined as one that is open for nighttime periods only, that is from 4:00 p.m. to 8:00 a.m. on the next day; it does not function as a common household for a family, although common bath and/or kitchen facilities are typically shared by inhabitants. Where authorized as a special use in Chapter 27.18, the emergency shelter is subject to the following: (a) limited to up to 14 persons who have been evaluated by persons experienced in shelter placement; (b) limited to not more than 14 consecutive days and not more that seven weeks in a year; (c) limited to housing only and shall not provide on-site medical care, laundry, day care, and/or employment assistance or counseling; (d) required to provide transportation for the inhabitants; (e) required to designate one person as a community liaison to receive and resolve community complaints. Pursuant to a special use permit designating different limitations and allowances the number of persons to be housed and/or the time limits for housing may be increased."
    },
    {
      "heading": "27.04.180 ENVIRONMENTAL DOCUMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.180",
      "text": "\"Environmental document\" means material, submitted in conformance with the current San Mateo Environmental Guidelines, which is designed to evaluate the environmental effects of a proposed project."
    },
    {
      "heading": "27.04.185 ERECT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.185",
      "text": "\"Erect\" means the act of placing or affixing a component of a structure upon or in the ground or upon another such component."
    },
    {
      "heading": "27.04.190 ESTABLISHMENT, BUSINESS.",
      "id": "/us/ca/cities/san-mateo/code/27.04.190",
      "text": "\"Business establishment\" means a separate place of business having the following characteristics: (1) The ownership and management of all operations conducted within such establishment is separate and distinct from the ownership and management of operations conducted within other establishments on the same or adjacent zoning plots; (2) Direct public access to such \"business establishment\" is separate and distinct from direct access to any other business establishment; (3) There is no direct public access from within such establishment to any other such establishment. When adjacent places of business lack any one of the aforesaid characteristics with respect to one another, they shall then be considered as a single \"business establishment\" for the purpose of this title."
    },
    {
      "heading": "27.04.195 FAMILY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.195",
      "text": "\"Family\" means a person or a group of persons living together and maintaining a common household."
    },
    {
      "heading": "27.04.197 FAST-FOOD AND DRIVE-IN ESTABLISHMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.04.197",
      "text": "\"Fast-food and drive-in establishments\" means those food service establishments offering any quick food service or goods for immediate consumption in vehicles, out-of-doors, or off the premises, in addition to such service within the establishment, characterized by two or more of (a) and any of (b). (a) (1) Limited and standardized fare; (2) food served in edible or disposable containers; and (3) predominantly self-service. (b) (1) A drive-up service window; (2) greater than four on-site employees; (3) greater than 500 square feet of public service area; and (4) greater than 1,200 square feet of gross floor area."
    },
    {
      "heading": "27.04.200 Floor Area.",
      "id": "/us/ca/cities/san-mateo/code/27.04.200",
      "text": "(a) Definitions. (1) Floor Area. Floor area means the sum of the gross horizontal areas of all principal and accessory buildings and above grade covered parking on a zoning plot. (2) Floor Area Ratio (FAR). Floor area ratio means the gross floor area of the buildings on a zoning plot divided by the net lot area. (b) Measurement, other than single-family dwellings in R1 zoning districts. (1) Floor area is measured from the exterior façade of the building's wall planes, from the centerline of party walls, or from a line three feet from the edge of an eave, whichever produces the largest floor area. Stories exceeding fifteen (15) feet in height shall be counted as additional floor area, with the exception that ground floor retail may be up to eighteen (18) feet in height measured from first finish floor to second finish floor before being counted as additional floor area. Floor area also includes all accessory structures on the site and basements that meet the definition in subsection (c)(6). (2) Exclusions. The following are not counted as floor area: (A) Covered or open courts, and atriums, on the ground floor, provided that the area is not used as dwelling, office, retailing, or required access; (B) In multiple-level buildings, covered courts, if the retailing uses are open to the public. Multiple-level stairwells and elevators shall be counted only as ground floor area; (C) Covered walkways and balconies; (D) First floors, mechanical areas, penthouse, and top floors are counted only once as floor area, regardless of height; (E) Bicycle parking facilities; (F) Floor area designated for day care centers accessory to and intended to serve a multi-family, commercial, office or manufacturing use. Such floor area may be located within the primary structure or may be in a freestanding structure accessory to the primary structure; (G) Covered parking for office use shall not be counted as floor area in areas delineated for exclusion within an adopted plan, such as the Mariner's Island Specific Plan or the Bay Meadows Specific Plan. (c) Measurement, for single-family dwellings in R1 zoning districts, shall include the following: (1) A covered structure or portion of a building where it has a horizontal or sloped covering which consists of 50% or more solid material. (2) All area enclosed within the walls of the principal structure (as measured from the outside perimeter of walls), and the area (or footprint) of any attached carports, covered balconies or porches (as measured from the outside perimeter of its support structures). (A) Exception: To encourage street frontage activity, the first 100 square feet of a covered front porch shall not be included as floor area. (3) The area of all detached accessory structures, regardless of the number of open sides, including: (A) Detached garages and carports; (B) Storage sheds and other similar structures; and (C) Covered patios or similar structures. (4) Any interior space where the vertical distance between the upper surface of the floor and the floor above is fifteen (15) feet or more shall be counted as twice the floor area. If there is no floor above the space, then the distance shall be measured to the underside of the roof structure. (5) Attic space is considered floor area when area \"A\" is at least 50% of areas \"A\" and \"B\" combined in the following plan-view diagram: (6) A basement is considered floor area when: (A) It is habitable space as defined in the current California Building Code, and (B) More than one-half the area of the outermost basement walls is above finished or pre-existing grade (whichever is lower), and the surface of the finished floor level above is either: (i) More than four (4) above finished or pre-existing grade (whichever is lower) for more than 50% of the total perimeter, and (ii) More than twelve (12) feet above finished or pre-existing grade (whichever is lower) at any point. (d) Off-Street Parking and Loading. Floor area for determining off-street parking and loading requirements as contained in Chapter 27.64, shall be based on physical floor space and shall not include the following: (1) Storage areas except for areas located within selling or working space such as counters, racks, and closets; (2) Utility areas including, but not limited to, elevator shafts, telephone switching rooms, stairwells, rest rooms, and heating and cooling rooms; (3) Accessory facilities to be used only by employees of the principal uses; (4) Off-street parking and loading facilities, including aisles, ramps, and maneuvering space; (5) Basement, attic, or mezzanine floor area other than area devoted to retailing activities, to the production of processing of goods, or to business or professional offices; (6) Floor area designated for day care centers accessory to and intended to serve a multi-family, commercial, office or manufacturing use. Such floor area may be located within the primary structure or may be in a freestanding structure accessory to the primary structure; (7) Floor Area Computed for Building Volume. Additional parking shall be required in the event of change of excluded floor areas into uses generating parking. (e) Interpretation. All interpretations of floor area shall be subject to the review and approval of the Zoning Administrator. (f) No change in the definition or calculation of floor area, except to the extent that the City Council expressly states that the change allows greater floor area, shall be construed to authorize an expansion of the allowable floor area of a building or structure, whether pursuant to Chapter 27.72 or otherwise."
    },
    {
      "heading": "27.04.205 FRONTAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.205",
      "text": "\"Frontage\" means all the property fronting on one side of a street between the nearest intersecting streets, or between a street and right-of-way, waterway, or some other similar barrier. "
    },
    {
      "heading": "27.04.210 FUEL BULK STATION.",
      "id": "/us/ca/cities/san-mateo/code/27.04.210",
      "text": "\"Fuel bulk station\" means a place where crude petroleum, gasoline, naphtha, benzene, benzol, kerosene, or other flammable liquid, which has a flash point at or below 187 degrees Fahrenheit, is stored for wholesale purposes and for distribution in bulk by a tank truck or otherwise."
    },
    {
      "heading": "27.04.211 GABLE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.211",
      "text": "\"Gable\" means the triangular wall enclosed by the sloping ends of a ridged roof."
    },
    {
      "heading": "27.04.212 GARAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.212",
      "text": "\"Garage\" means a fully enclosed and covered attached or detached structure accessory to a residential use intended for storage of one or more motor vehicles."
    },
    {
      "heading": "27.04.215 GOLF COURSE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.215",
      "text": "\"Golf course\" means public, semipublic, or private grounds over which the game of golf is played, including accessory buildings and land uses incidental thereto, and consisting of at least 60 acres for each standard nine-hole course; and 25 acres for each nine-hole \"par 3\" course."
    },
    {
      "heading": "27.04.220 GRADE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.220",
      "text": "\"Grade\" is the elevation of the finished surface of the ground not resulting from a decorative mound or beam at any point along an exterior wall of a building. (a) \"Established grade\" means the top of curb grade at the lot lines established by the Director of Public Works, or otherwise established by law."
    },
    {
      "heading": "27.04.225 GUEST HOUSE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.225",
      "text": "\"Guest house\" means a detached accessory building located on the same premises with the principal building, containing living quarters for use by nonpaying guests of the occupants of the premises."
    },
    {
      "heading": "27.04.230 GUEST, PAYING.",
      "id": "/us/ca/cities/san-mateo/code/27.04.230",
      "text": "\"Paying guest\" means any person renting one or more rooms or portions thereof for living purposes. The room(s) involved shall have an internal connection with the principal dwelling unit and shall not have independent cooking facilities."
    },
    {
      "heading": "27.04.235 HIGH-RISE BUILDING.",
      "id": "/us/ca/cities/san-mateo/code/27.04.235",
      "text": "\"High-rise building\" means any building which is more than 50 feet in height as measured from average grade."
    },
    {
      "heading": "27.04.240 HOME OCCUPATION.",
      "id": "/us/ca/cities/san-mateo/code/27.04.240",
      "text": "\"Home occupation\" means an accessory business conducted in a dwelling unit solely by its occupants in a manner incidental to the residential use of the dwelling, in accordance with the provisions of Section 27.16.040."
    },
    {
      "heading": "27.04.245 HOSPITAL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.245",
      "text": "\"Hospital\" means an institution devoted primarily to the maintenance and operation of facilities for the medical or surgical care of patients for 24 hours or more. The term \"hospital,\" as used in this title, does not apply to institutions operating solely for the treatment of mentally ill persons, drug addicts, liquor addicts, or other types of cases necessitating confinement of patients, and the term \"hospital\" shall not be used for convalescent, nursing, shelter or boarding homes."
    },
    {
      "heading": "27.04.250 HOTEL, APARTMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.250",
      "text": "\"Apartment hotel\" means a building containing dwelling units or individual guest rooms, the majority of which are for permanent guests. Maid and janitor service may be provided but kitchen facilities are not necessarily included."
    },
    {
      "heading": "27.04.255 HOTEL, MOTEL, MOTOR HOTEL, INN OR AUTO COURT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.255",
      "text": "\"Hotel,\" \"motel,\" \"motor hotel,\" \"inn\" or \"auto court\" means an establishment consisting of one building or a group of attached or detached buildings containing lodging accommodations designed for use by transients, or travelers, or temporary guests. Facilities provided may include maid service, laundering of linen used on the premises, telephone and secretarial or desk service, meal and beverage service, meeting rooms, incidental merchandise sales, barber and beauty shops, kitchens, and other incidental services and facilities."
    },
    {
      "heading": "27.04.257 COMMUNITY RELATIONS COMMISSION.",
      "id": "/us/ca/cities/san-mateo/code/27.04.257",
      "text": "\"Community Relations Commission\" means the City Community Relations Commission of the City of San Mateo, California."
    },
    {
      "heading": "27.04.260 KENNEL, COMMERCIAL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.260",
      "text": "\"Commercial kennel\" means any lot or premises or portion thereof on which dogs, cats, and other household domestic animals are maintained, boarded, bred or cared for in return for compensation or kept for sale."
    },
    {
      "heading": "27.04.265 LABORATORY, COMMERCIAL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.265",
      "text": "\"Commercial laboratory\" means a place devoted to experimental study, such as testing and analyzing. Manufacturing, assembly, or packaging of products is not included within this definition."
    },
    {
      "heading": "27.04.267 LANDSCAPING, NATURAL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.267",
      "text": "\"Natural landscaping\" means all living plant material installed at ground level, in pots or planters."
    },
    {
      "heading": "27.04.268 LIMITED PARKING ZONE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.268",
      "text": "\"Limited parking zone\" means an area within the Central Parking and Improvement District recognized by action of the City Council which is intended to accommodate high levels of pedestrian and visitor traffic by limiting the amount of off-street parking supplied in the zone."
    },
    {
      "heading": "27.04.270 LODGING OR ROOMING HOUSE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.270",
      "text": "\"Lodging or rooming house\" means a building where lodging alone is provided for compensation for residents not functioning as a common household."
    },
    {
      "heading": "27.04.275 LOT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.275",
      "text": "\"Lot\" means a parcel of land designated on a recorded subdivision map as a lot. (a) \"Corner lot\" means a lot or parcel of land situated at the junction of and abutting on two or more intersecting streets; or a lot or parcel of land at the point of deflection in alignment of a single street, the interior angle of which is 135 degrees or less. (b) \"Reversed corner lot\" means a corner lot, the rear of which abuts upon the side of another lot, whether across an alley or not. (c) \"Interior lot\" means a lot other than a corner lot or reversed corner lot. (d) \"Through lot\" means a lot which is not a corner lot, that has frontage on two parallel or approximately parallel streets. On a through lot both property lines abutting a street shall be deemed front lot lines."
    },
    {
      "heading": "27.04.280 LOT AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.04.280",
      "text": "(a) \"Net lot area\" means the area of a horizontal plane bounded by the front, side, and rear lot lines. (b) \"Gross lot area\" means the net lot area plus the area between the boundaries of the lot and the centerline of adjoining public streets or alleys."
    },
    {
      "heading": "27.04.285 LOT COVERAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.285",
      "text": "\"Lot coverage\" means the area of a zoning plot occupied by the principal building(s), accessory building(s), covered patio(s), and any open parking or loading area(s)."
    },
    {
      "heading": "27.04.290 LOT DEPTH.",
      "id": "/us/ca/cities/san-mateo/code/27.04.290",
      "text": "\"Lot depth\" means the mean horizontal distance between the front and rear lot lines of a lot measured within the lot boundaries, or in the case of a through lot, the horizontal distance between the two front lot lines."
    },
    {
      "heading": "27.04.295 LOT FRONTAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.295",
      "text": "\"Lot frontage\" means that boundary of a lot along a public street."
    },
    {
      "heading": "27.04.300 LOT LINE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.300",
      "text": "\"Lot line\" means a property boundary line of any lot held in separate ownership; except that where any portion of the lot extends into the abutting street or alley, the lot line shall be deemed to be the street or alley line. (a) \"Front lot line\" means the front property line of a zoning plot. On a corner lot, the owner may elect either property line abutting a street as the front lot line. (b) \"Rear lot line\" means the lot line(s) most nearly parallel to and most remote from the front lot line. (c) \"Side lot line\" means lot line(s) other than front or rear lot lines. (d) \"Interior lot line\" means a side or rear lot line common with another lot."
    },
    {
      "heading": "27.04.305 LOT WIDTH.",
      "id": "/us/ca/cities/san-mateo/code/27.04.305",
      "text": "\"Lot width\" means the horizontal distance between the side lot lines measured at right angles to the lot depth at any point within the required front yard setback."
    },
    {
      "heading": "27.04.310 MARQUEE—CANOPY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.310",
      "text": "\"Marquee\" or \"canopy\" means a rooflike structure of a permanent nature which projects from the wall of a building and overhangs the public way, and is designed and intended to protect pedestrians from adverse weather conditions."
    },
    {
      "heading": "27.04.311 MAUSOLEUM.",
      "id": "/us/ca/cities/san-mateo/code/27.04.311",
      "text": "\"Mausoleum\" means an above-ground grave and structure used primarily for full body entombment."
    },
    {
      "heading": "27.04.313 MINOR FAÇADE MODIFICATION.",
      "id": "/us/ca/cities/san-mateo/code/27.04.313",
      "text": "\"Minor façade modification\" means changes or alterations to the exterior of an existing building where no increase in the square footage of the building will occur. This includes, but is not limited to, changes in building materials, alterations, additions or elimination of existing doors, windows, awnings and other building elements, and changes to architectural features, such as the building cornice, roof or parapet."
    },
    {
      "heading": "27.04.314 MONUMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.314",
      "text": "\"Monument\" means a tombstone, headstone, or similar grave marker that does not contain human remains."
    },
    {
      "heading": "27.04.315 MOTOR FREIGHT TERMINAL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.315",
      "text": "\"Motor freight terminal\" means a building in which freight brought to the building by motor truck is assembled and sorted for routing in intrastate and interstate shipment by motor truck."
    },
    {
      "heading": "27.04.320 MOTOR VEHICLE REPAIR, MAJOR.",
      "id": "/us/ca/cities/san-mateo/code/27.04.320",
      "text": "\"Major motor vehicle repair\" means engine rebuilding or major reconditioning of worn or damaged motor vehicles or trailers; collision service, including body, frame or fender straightening or repair; and overall painting of vehicles within an enclosed building."
    },
    {
      "heading": "27.04.325 MOTOR VEHICLE REPAIR, MINOR.",
      "id": "/us/ca/cities/san-mateo/code/27.04.325",
      "text": "\"Minor motor vehicle repair\" means incidental repairs, replacement of parts, and motor service to motor vehicles, but does not include any operation specified under Section 27.04.320."
    },
    {
      "heading": "27.04.330 NONCONFORMING USE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.330",
      "text": "\"Nonconforming use\" means any building, structure or land lawfully occupied by a use or lawfully established at the time of the adoption of this title or amendments thereto, which does not conform after the passage of this title or amendments hereto with the use regulations of this title."
    },
    {
      "heading": "27.04.335 NURSERY, DAY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.335",
      "text": "\"Day nursery\" means a community care or lodging facility as defined in Section 27.04.130."
    },
    {
      "heading": "27.04.340 NURSING, HOSPICE, AND/OR CONVALESCENT FACILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.340",
      "text": "\"Nursing, hospice, and/or convalescent facility\" means a facility for the in-patient care of sick, injured, aged, or infirmed, or dying persons. It is a place of rest for those who are bedfast, or require considerable nursing care, and may include facilities for the treatment of sickness, or injuries, or for minor surgery and emergency treatment of the resident patients."
    },
    {
      "heading": "27.04.342 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.04.342",
      "text": "\"Off-street parking\" means parking stalls provided beyond the right-of-way of a street or highway."
    },
    {
      "heading": "27.04.344 ON-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.04.344",
      "text": "\"On-street parking\" means parking stalls provided within the right-of-way of a street or highway."
    },
    {
      "heading": "27.04.345 OPEN SALES LOT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.345",
      "text": "\"Open sales lot\" means any land used for the purpose of buying, selling or trading new or secondhand passenger cars, trucks, motor scooters, motorcycles, boats, trailers, aircraft, or similar articles."
    },
    {
      "heading": "27.04.350 OPEN SPACE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.350",
      "text": "\"Open space\" means that portion of a site that has not been covered by buildings, structures, or parking areas or driveways. Open space areas include, but are not limited to, parks, playgrounds, beaches and waterways. \"Usable open space\" means outdoor area on the ground, balcony, deck, porch, or roof which is designed, improved, developed and maintained to be used for outdoor living, recreation, or garden purposes. However, for purposes of receiving a bonus to increase the floor area ratio (FAR), not more than 10% of improved roof decks, roof gardens or roof recreation facilities will be granted. The minimum standards for a roof used for gardens, decks or recreational purposes shall be established by resolution of the City Council. Further, off-street parking and loading areas, driveways, and required sidewalks are not counted in calculating usable open space. (a) Private Usable Open Space. (1) \"Residential private usable open space\" means open space adjacent to a dwelling unit or units designed and reserved for the use of the occupants. (2) \"Commercial/executive private usable open space\" means open space which is improved for the use of employees and guests of the development, such as an inner courtyard. (b) Common Usable Open Space. (1) \"Residential common usable open space\" means open space accessible to all occupants of a residential complex. Pedestrian and bicycle paths, swimming pools, and tennis courts are typical forms of residential common usable open space. (2) \"Commercial/executive common usable open space\" means open space in the form of a plaza, square, court, or other urban space which is at least 75% open to the sky, free from automotive traffic, and accessible to the public at large."
    },
    {
      "heading": "27.04.351 ORIEL BAY WINDOW.",
      "id": "/us/ca/cities/san-mateo/code/27.04.351",
      "text": "\"Oriel bay window\" means a window which projects and is cantilevered from a building wall, is not supported by its own foundation, and which does not provide interior floor area."
    },
    {
      "heading": "27.04.355 OWNER.",
      "id": "/us/ca/cities/san-mateo/code/27.04.355",
      "text": "\"Owner\" means one or more persons holding record title to the freehold interest in a lot or parcel of real property."
    },
    {
      "heading": "27.04.356 Paving",
      "id": "/us/ca/cities/san-mateo/code/27.04.356",
      "text": "(a) Paving\" means solid, pavement materials that includes both pervious and non-pervious surfaces. Examples of paving include asphalt, concrete, brick, tile, decomposed granite, permeable concrete, and grass-cells. (b) \"Non-pervious\" or \"impervious\" surface means any surface or material that does not allow the passage of water through the material and into the underlying soil. (c) \"Pervious\" surface means any surface or material that allows the passage of water through the material and into the underlying soil."
    },
    {
      "heading": "27.04.357 PARCEL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.357",
      "text": "\"Parcel\" means an area of land which has been legally subdivided."
    },
    {
      "heading": "27.04.358 PARCEL COVERAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.358",
      "text": "(a) In E Districts and CBD, parcel coverage means the portion of a parcel permitted to be developed with buildings, structures, patios and automobile parking and loading facilities. (b) In R4-D and R6-D Districts, parcel coverage means the portion of a parcel permitted to be developed with buildings, enclosed or structured parking."
    },
    {
      "heading": "27.04.360 PARCEL DELIVERY STATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.04.360",
      "text": "\"Parcel delivery station\" means a building in which commodities sold at retail within the area, and packaged by the retailer, are assembled and routed for delivery to retail customers located within the area."
    },
    {
      "heading": "27.04.363 PARKING EXPANSION ZONE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.363",
      "text": "\"Parking expansion zone\" means an area within the Central Parking and Improvement District recognized by action of the City Council which is intended to accommodate long-term parking generated by uses within the limited parking zone."
    },
    {
      "heading": "27.04.365 PARKING FACILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.365",
      "text": "\"Parking facility\" means an off-street area, whether open or enclosed, other than a showroom or sales lot, used to store motor vehicles on a daily basis, but not including the storage of dismantled or wrecked motor vehicles or parts thereof. (a) \"Commercial\" means provided by a private party for a fee; (b) \"Private\" means provided for the use of residents, customers or employees primarily in response to code requirements; (c) \"Public\" means provided by the City, the use of which may or may not be subject to a fee; (d) \"Parking lot\" means an open, at-grade parking area, which may be commercial, public or private; (e) \"Parking garage\" means an enclosed parking structure provided above or below grade, which may be commercial, public or private."
    },
    {
      "heading": "27.04.370 PERFORMANCE STANDARD.",
      "id": "/us/ca/cities/san-mateo/code/27.04.370",
      "text": "\"Performance standard\" means a criterion to control noise, odor, smoke, toxic or noxious matter, vibration, fire and explosive hazards, or glare or heat generated by or inherent in uses of land or buildings."
    },
    {
      "heading": "27.04.375 PHILANTHROPIC INSTITUTION.",
      "id": "/us/ca/cities/san-mateo/code/27.04.375",
      "text": "\"Philanthropic institution\" means a benevolent or charitable organization not organized or existing for profit; but not including mental institutions."
    },
    {
      "heading": "27.04.380 PLANNED DEVELOPMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.04.380",
      "text": "\"Planned developments\" means a use or combination of uses planned for a single tract of land to be developed as a unit according to the provision of Chapter 27.62."
    },
    {
      "heading": "27.04.382 PLANNING APPLICATION (PA).",
      "id": "/us/ca/cities/san-mateo/code/27.04.382",
      "text": "\"Planning application\" means the written request for approval of a project and the supporting documents, reports, data, maps and other information, required to consider and review the project, as prescribed in Section 27.08.010."
    },
    {
      "heading": "27.04.385 PLANNING COMMISSION.",
      "id": "/us/ca/cities/san-mateo/code/27.04.385",
      "text": "\"Planning Commission\" means the City Planning Commission of the City of San Mateo, California."
    },
    {
      "heading": "27.04.386 PLATELINE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.386",
      "text": "\"Plateline\" means the line established by the horizontal girder which supports the trusses or rafters of a roof."
    },
    {
      "heading": "27.04.390 PORCH—LANAI.",
      "id": "/us/ca/cities/san-mateo/code/27.04.390",
      "text": "\"Porch\" or \"lanai\" means a covered entrance to a building or a roofed-over structure projecting out from the exterior wall or walls of a main structure and commonly open to the weather in part."
    },
    {
      "heading": "27.04.395 PRINCIPAL USE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.395",
      "text": "\"Principal use\" means the main use of land or buildings as distinguished from a subordinate or accessory use."
    },
    {
      "heading": "27.04.397 PRIMARY BENEFIT ZONE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.397",
      "text": "\"Primary benefit zone\" or \"PBZ\" means any parcel within the Central Parking and Improvement District (C.P.I.D.) that is located within 500 feet of a C.P.I.D. parking facility as identified by the official C.P.I.D. map of the City."
    },
    {
      "heading": "27.04.398 PRIMARY PEDESTRIAN STREET.",
      "id": "/us/ca/cities/san-mateo/code/27.04.398",
      "text": "\"Primary pedestrian street\" means a street or street segment which provides a means of circulation intended primarily for destinations within the retail core of the central business district, as recognized by action of the City Council."
    },
    {
      "heading": "27.04.399 PRIMARY PERIPHERAL STREET.",
      "id": "/us/ca/cities/san-mateo/code/27.04.399",
      "text": "\"Primary peripheral street\" means a street or street segment which provides a main access route to and around the retail core of the central business district and intended primarily for through-traffic, as recognized by action of the City Council."
    },
    {
      "heading": "27.04.400 PRIVATE SCHOOL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.400",
      "text": "\"Private school\" means an educational institution, not under public administration, excluding mechanical or industrial trade schools."
    },
    {
      "heading": "27.04.404 PUBLIC SERVICE AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.04.404",
      "text": "\"Public service area\" means that portion of a building or structure used or which may be used by patrons for the purposes of eating, drinking or waiting for service, including dance floors and area outside the building or structure intended to be used by patrons for the purposes of eating or drinking."
    },
    {
      "heading": "27.04.405 PUBLIC UTILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.405",
      "text": "\"Public utility\" means any person, or municipal department, duly authorized to furnish, under public regulation to the public, electricity, gas, steam, telephone, transportation, or water."
    },
    {
      "heading": "27.04.410 RADIO OR TELEVISION TRANSMITTING PLANT OR STATION.",
      "id": "/us/ca/cities/san-mateo/code/27.04.410",
      "text": "\"Radio or television transmitting plant or station\" means a building and equipment used for the transmission or reception of messages by wireless, and for the transmission of programs over the air without use of wires."
    },
    {
      "heading": "27.04.415 RAILROAD RIGHT-OF-WAY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.415",
      "text": "\"Railroad right-of-way\" means a strip of land with tracks and auxiliary facilities for track operation; but not including depot loading platforms, stations, train sheds, warehouses, car shops, car yards, locomotive shops, water towers, etc."
    },
    {
      "heading": "27.04.417 RECREATIONAL VEHICLE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.417",
      "text": "\"Recreational vehicle\" means a vehicle primarily designed as temporary living quarters, recreational, camping, or travel use."
    },
    {
      "heading": "27.04.418 RECREATIONAL VEHICLE (RV) STORAGE FACILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.418",
      "text": "\"RV storage facility\" means a zoning plot upon which two or more recreational vehicles may be stored for a fee when not in use."
    },
    {
      "heading": "27.04.419 RECYCLING CENTER.",
      "id": "/us/ca/cities/san-mateo/code/27.04.419",
      "text": "A \"recycling center\" is a facility for the collection of recyclable materials such as metals, glass, plastic, and paper. Such a facility shall not do processing except limited bailing, batching and sorting of materials. Recycling facilities include: bins, boxes, cans, kiosk type structures, bulk reverse vending machines, trucks, trailers, or vans."
    },
    {
      "heading": "27.04.420 RECYCLING COLLECTION AREAS.",
      "id": "/us/ca/cities/san-mateo/code/27.04.420",
      "text": "A \"recycling collection area\" is any indoor or outdoor spaced allocated for collecting and loading recyclable materials."
    },
    {
      "heading": "27.04.421 REPLACEMENT VALUE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.421",
      "text": "\"Replacement value\" means the current construction cost for the replacement of an existing building, structure, or portion thereof, including accessory facilities and other parts of an established use."
    },
    {
      "heading": "27.04.425 RESTAURANT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.425",
      "text": "\"Restaurant\" means any land, building, or part thereof, other than a boarding house, or bed and breakfast inn, where food, including the serving of alcoholic and/or non-alcoholic beverages, is provided for consumption on premises where tables, counters, benches, or other public seating facilities are provided, such as a café, bakery, cafeteria, coffee shop, lunchroom, delicatessen, drive-in stand, tearoom and dining room."
    },
    {
      "heading": "27.04.427 REVERSE VENDING MACHINES.",
      "id": "/us/ca/cities/san-mateo/code/27.04.427",
      "text": "A \"reverse vending machine\" is a mechanical device which accepts one or more types of empty beverage containers, including aluminum cans, glass and plastic bottles, and cartons, and issues a cash refund or a redeemable credit slip. \"Bulk reverse vending machines\" are those machines which exceed 50 cubic feet in size or exceed eight feet in height."
    },
    {
      "heading": "27.04.430 SANITARIUM.",
      "id": "/us/ca/cities/san-mateo/code/27.04.430",
      "text": "\"Sanitarium\" means a building and premises in and on which two or more sick, injured or infirm persons are regularly housed or intended to be housed for compensation, not including hospitals."
    },
    {
      "heading": "27.04.435 SERVICE BAY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.435",
      "text": "\"Service bay\" means an enclosed work station capable of accommodating one vehicle for automotive repair."
    },
    {
      "heading": "27.04.436 SHOPPING CENTER.",
      "id": "/us/ca/cities/san-mateo/code/27.04.436",
      "text": "\"Shopping center\" means two or more retail and general commercial uses with parking facilities which may be shared. (a) \"Community shopping center\" means a shopping center generally between 20,000 and 100,000 square feet of gross floor area, capable of supporting two or more retail or commercial businesses. (b) \"Regional shopping center\" means a shopping center generally totaling more than 100,000 square feet of gross floor area, including one or more anchor department stores."
    },
    {
      "heading": "27.04.437 SOLARIUM.",
      "id": "/us/ca/cities/san-mateo/code/27.04.437",
      "text": "\"Solarium\" means a projection from the building face which is fully enclosed by a transparent or translucent material."
    },
    {
      "heading": "27.04.440 SPECIAL USE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.440",
      "text": "\"Special use\" means a use, either public or private, which is not classified as a permitted use in any particular district or districts, but which may be necessary or desirable to permit in a given district, subject to certain conditions and stipulations required to effect compatibility with existing or permitted uses in the area wherein the specific use is proposed to be located."
    },
    {
      "heading": "27.04.445 STORY.",
      "id": "/us/ca/cities/san-mateo/code/27.04.445",
      "text": "(a) \"Story\" means the portion of a building included between the upper surface of any floor and the upper surface of the floor next above, or if there is no floor above, then the space between the upper surface of the floor and the ceiling or roof above it, or a maximum vertical distance of 13 feet. Exclusions are delineated in the definition of floor area. (b) Yard Requirements. When related to the number of stories of the building, the required yard shall be the building height divided by the story interval of 13 feet. Fractional remainders, over the last complete story, shall be counted as an additional story. The space below the first finished floor will not be counted as a story, if it is less than four feet above grade, for more than 50% of the total building perimeter. "
    },
    {
      "heading": "27.04.450 STREET.",
      "id": "/us/ca/cities/san-mateo/code/27.04.450",
      "text": "\"Street\" means a public or private way open to vehicular and pedestrian travel other than a freeway or other restricted access way or alley."
    },
    {
      "heading": "27.04.455 STREET LINE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.455",
      "text": "\"Street line\" means a line separating an abutting lot, piece or parcel from a street."
    },
    {
      "heading": "27.04.460 STRUCTURAL ALTERATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.04.460",
      "text": "\"Structural alterations\" means any change other than incidental repairs to a building or structure, involving foundations, bearing walls, columns, beams or girders."
    },
    {
      "heading": "27.04.465 STRUCTURE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.465",
      "text": "\"Structure\" means anything constructed or erected, except fences not exceeding six feet in height, which requires permanent location on the ground or is attached to something having location on the ground."
    },
    {
      "heading": "27.04.470 SWIMMING POOL.",
      "id": "/us/ca/cities/san-mateo/code/27.04.470",
      "text": "\"Swimming pool\" means any pool over 24 inches in depth, or with a surface area exceeding 100 square feet, used or intended to be used for swimming or bathing."
    },
    {
      "heading": "27.04.475 TAVERN—LOUNGE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.475",
      "text": "\"Tavern\" or \"lounge\" means a building where alcoholic beverages are sold for consumption on the premises, not including restaurants where the principal business is serving food."
    },
    {
      "heading": "27.04.480 TERRACE, OPEN.",
      "id": "/us/ca/cities/san-mateo/code/27.04.480",
      "text": "\"Open terrace\" means a plane or platform which is located adjacent to one or more faces of the principal structure and which is constructed not more than four feet in height above the average level of the adjoining ground."
    },
    {
      "heading": "27.04.485 TRAILER.",
      "id": "/us/ca/cities/san-mateo/code/27.04.485",
      "text": "\"Trailer\" means a vehicle without motive power used or adaptable for living, sleeping, business or storage purposes, having no foundation other than wheels, blocks, skids, jacks, horses, or skirting, which does not meet building code requirements and has been or reasonably may be equipped with wheels or other devices for transporting the structure from place to place. The term \"trailer\" includes \"camp car\" and \"house car.\" A permanent foundation shall not change its character unless the entire structure is erected and maintained in accordance with prevailing laws."
    },
    {
      "heading": "27.04.490 USE.",
      "id": "/us/ca/cities/san-mateo/code/27.04.490",
      "text": "\"Use\" means the purpose for which land or a building thereon is designed, arranged or intended, or for which it is occupied or maintained, let or leased."
    },
    {
      "heading": "27.04.492 VALET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.04.492",
      "text": "\"Valet parking\" means automobile parking service provided by an attendant for the patrons of commercial establishments."
    },
    {
      "heading": "27.04.494 WETBAR.",
      "id": "/us/ca/cities/san-mateo/code/27.04.494",
      "text": "\"Wetbar\" means a counter surface located within a common living area room in a dwelling unit that is equipped with one sink of any size but no other appliances or fixtures typically used in food preparation."
    },
    {
      "heading": "27.04.495 YARD.",
      "id": "/us/ca/cities/san-mateo/code/27.04.495",
      "text": "\"Yard\" means an open space on the same zoning plot with a principal building or group of buildings, which is unoccupied and unobstructed from its lowest level upward, except as otherwise permitted by this title. (a) \"Front yard\" means a yard extending across the full width of the zoning plot and lying between the front property line and the nearest line of the principal building. (b) \"Rear yard\" means a yard extending across the full width of the zoning plot and lying between the rear property line and the nearest line of the principal building. (c) \"Side yard\" means the part of a yard lying between the nearest line of the principal building and a side lot line, and extending from the required front yard (or from the front line, if there is no required front yard) to the required rear yard. "
    },
    {
      "heading": "27.04.500 ZONING MAPS.",
      "id": "/us/ca/cities/san-mateo/code/27.04.500",
      "text": "\"Zoning maps\" means the map or maps incorporated into this title designating zoning districts."
    },
    {
      "heading": "27.04.505 ZONING PLOT.",
      "id": "/us/ca/cities/san-mateo/code/27.04.505",
      "text": "\"Zoning plot\" means a plot of ground consisting of one or more lots or parcels on which a common improvement has been authorized under this title."
    }
  ],
  "Chapter 27.06 ADMINISTRATION": [
    {
      "heading": "27.06.010 APPROVAL BODIES.",
      "id": "/us/ca/cities/san-mateo/code/27.06.010",
      "text": "There shall be three approval bodies for planning applications: (a) Zoning Administrator. The Director of Community Development, or designee, shall be Zoning Administrator, and the Department of Community Development shall be the office of the Zoning Administrator. The Zoning Administrator shall possess the powers and duties as described in this chapter. (b) Planning Commission. The Planning Commission shall be organized according to Section 2.24.010 and shall possess the powers and duties described in this Title in addition to those contained in Section 2.24.030. (c) City Council. The City Council shall consider planning applications in the manner described in this Title. (d) Each approval body shall adopt rules for holding meetings and conducting business. The rules adopted by the Zoning Administrator shall be subject to the approval of the Planning Commission."
    },
    {
      "heading": "27.06.020 ZONING ADMINISTRATOR—POWERS AND DUTIES.",
      "id": "/us/ca/cities/san-mateo/code/27.06.020",
      "text": "The Zoning Administrator shall enforce the provisions of this Title, and shall: (a) Conduct such inspections of buildings, structures, and use of land as are necessary to determine compliance with the terms of this Title; (b) Establish, with the approval of the Council, and administer rules for the conduct of the Zoning Administrator's office; (c) Maintain permanent and current records of documents and proceedings under this Title; (d) Provide and maintain a continuing program of education and public information on zoning matters; (e) Recommend abatement of violations of this Title and aid in prosecution thereof; (f) Receive, file, and transmit to the appropriate approval body all planning applications and all appeals which the designated approval body is authorized to review or to take final action upon under the provisions of this Title; (g) Interpret provisions of the zoning ordinance, subject to appeal of the decision to the Planning Commission; (h) Have the authority to review and approve, conditionally approve, or disapprove the following types of projects, provided that the projects do not result in any significant impacts pursuant to the California Environmental Quality Act (CEQA), subject to public notice and to appeal of the final action to the Planning Commission: (1) Site plan and architectural review for projects that incorporate: (A) Up to twenty-five (25) residential dwelling units that meet objective design standards as adopted by resolution of the City Council; or (B) Up to five (5) residential dwelling units that do not meet objective design standards as adopted by resolution of the City Council; or (C) Up to 10,000 square feet of non- residential development; or (D) Other minor site improvements including but not limited to parking lots, landscaping, recreation facilities, accessory structures, recycling collection areas, circular driveways in R1, R2 districts; (E) Fences over seven (7) feet and those over three (3) feet when located in a front yard and/or street side yard setback or within forty-five (45) feet of a street intersection line, authorized by Chapter 27.84. (F) Freestanding signs. (2) Site development permits for removal of major vegetation required for the construction of projects that require Zoning Administrator review and approval, or grading of five thousand (5,000) cubic yards or less under Chapter 23.40. (3) Variances as authorized by Chapter 27.78, for single-family, accessory dwelling units, duplex dwellings, or residential projects with up to six (6) residential dwelling units. (4) Temporary use permits authorized by Chapter 27.74. (5) Modifications authorized by Chapter 27.08. (6) Special permits to allow the following: (A) Recycling facilities subject to regulations established in Chapter 27.69; (B) Plumbing in detached accessory buildings in the R-1 zone, as authorized under Chapter 27.18 (C) Substantial removal of existing residences in an R-1 zoning district; (D) Temporary real estate sales offices, as authorized under Chapters 26.04 and 27.18; (E) Swimming pools, hot tubs, and spas located in required front or street side yards, as authorized under Chapter 27.18; and (F) Additional floor area ratio in the R-3 District, as authorized under Chapter 27.22. (7) Concurrent development of two or more contiguous lots or parcels of real property in R-1 and R-2 districts. (8) Parcel Maps without exceptions as authorized by Title 26 (Subdivision). (9) Single-Family Dwelling Design Review (SFDDR) Applications. (10) City projects that meet the following criteria: (A) The project was conceptually approved as part of, or approved concurrent with, a Master Plan, program document, or project planning document that is in effect and has been previously approved by the City Council; and (B) The project does not propose major changes from previous City Council approval; and (C) The project would not result in a significant environmental impact pursuant to the California Environmental Quality Act (CEQA). (i) Notwithstanding the above, the Zoning Administrator may refer the application to the Planning Commission for hearing and action when it is unclear whether the necessary findings for project approval can be made."
    },
    {
      "heading": "27.06.030 DEVELOPMENT REVIEW BOARD—POWERS AND DUTIES.",
      "id": "/us/ca/cities/san-mateo/code/27.06.030",
      "text": "The Board shall review and provide recommendations on all planning applications."
    },
    {
      "heading": "27.06.040 PLANNING COMMISSION—JURISDICTION.",
      "id": "/us/ca/cities/san-mateo/code/27.06.040",
      "text": "(a) The Commission shall review and take final action, subject to appeal to the Council, upon all applications for: (1) Appeals from the decisions of the Zoning Administrator; (2) Special use permits other than for high rise buildings, or those identified under Section 27.06.020(h)(6); (3) Site Plan and Architectural Review for projects that incorporate: (A) Twenty-six (26) or more residential dwelling units that meet objective design standards as adopted by resolution of the City Council; or (B) Six (6) or more residential dwelling units that do not meet objective design standards as adopted by resolution of the City Council; or (C) Over 10,000 square feet of non-residential development. (4) Site Development Planning Applications involving grading of more than five thousand (5,000) cubic yards under Section 23.40; (5) Tentative Maps and Parcel Maps with exceptions under Title 26 (Subdivisions); (6) Applications which are accompanied by environmental impact reports, other than reclassifications, planned developments, special use permits for high rise buildings, and general plan amendments; (7) Release of conditions or easements recorded by the City under Section 27.08.045. (8) Modifications under Section 27.08.080(b). (9) Variances as authorized in Section 27.78.040 for planning applications for structures other than single-family and duplex. (10) Planned signing districts and freestanding signs over eight (8) feet in height. (b) The Commission shall review and make recommendations to the Council upon all applications for reclassifications, planned developments, site plan and architectural review for buildings exceeding 55 feet in height, General Plan amendments, projects which are fully or partially funded by the City and otherwise require Planning Commission review, and projects which include as part of the site any parcel of land which is in whole or in part subject to the tidelands trust provisions of State law. (c) The Commission may, on its own initiative, recommend to the Council that proceedings be initiated for an amendment, supplement, change or repeal of the whole or any portion of this Title, provided that public hearings thereon shall be held in the manner prescribed in this Title. The Commission shall periodically initiate a comprehensive review of the provisions of this Title and make a report of its findings to the Council."
    },
    {
      "heading": "27.06.050 COUNCIL CONSIDERATION AND DETERMINATION.",
      "id": "/us/ca/cities/san-mateo/code/27.06.050",
      "text": "The Council shall take final action on: (a) Appeals from the decisions of the Planning Commission; (b) Reclassifications; (c) Planned Developments; (d) Site Plan and Architectural Review for buildings exceeding 55 feet in height; (e) General Plan Amendments; (f) Historic Building Survey Amendment; (g) Historic Building Demolition Permit; (h) Every project which includes as part of the site any parcel of land which is in whole or in part subject to the tidelands trust provisions of State law; (i) Projects that are fully or partially funded by the City; (j) Downtown Economic Development Permit; and (k) The initiation and enaction of ordinances, including interim zoning ordinances/moratoria, without having to file a planning application."
    },
    {
      "heading": "27.06.060 MULTIPLE APPROVAL REQUESTS.",
      "id": "/us/ca/cities/san-mateo/code/27.06.060",
      "text": "When a planning application is comprised of multiple development approval requests, including one or more which could be final with one approval body and one or more which could be final only with another approval body, the approval body with the superior level of authority shall consider and act upon the entire planning application. If any portion or all of a multiple development approval request is appealed, the entire planning application shall be considered upon appeal."
    },
    {
      "heading": "27.06.070 SUBPOENAS—OATHS.",
      "id": "/us/ca/cities/san-mateo/code/27.06.070",
      "text": "The City Council and Planning Commission shall each have the power to issue subpoenas for, and to require the attendance of witnesses, the production of records and documents and to administer oaths and certify to all official acts under this Title."
    },
    {
      "heading": "27.06.080 STATE PLANNING AND ZONING REGULATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.06.080",
      "text": "(a) Chapters 3 and 4 of Title 7 of the California Government Code, commencing with Section 65100 thereof, are incorporated into this Title and made a part hereof by this reference, with the following exceptions: (1) Amendments to the general plan may be processed simultaneously with related zoning amendments and/or discretionary permits; and (2) There shall be no limit on the number of times the general plan may be amended in a calendar year; (3) No notice required to be published need be published in more than one issue of any newspaper; (4) Procedures for the enactment of zoning ordinances, including interim zoning ordinances/moratoria, are not incorporated; and (5) Government Code section 65863 is not incorporated by reference. (b) In the event of conflicts now or in the future, between these provisions of the California Government Code and City ordinances, resolutions, or Council policy, the latter shall prevail."
    },
    {
      "heading": "27.06.090 DEVELOPER CONTRIBUTIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.06.090",
      "text": "The Council may adopt by resolution from time to time a developer's contribution policy to be applied in zoning and land-use administration. New or changed developments often place an increased demand upon public facilities. When additional, new, or expanded public improvements are needed to support a new or changed land use or development, these improvements should be paid for on an equitable basis by the developer. New land-use projects should not require the expenditure of tax moneys to support the project development. The required improvements should be compatible and in continuity with adjacent, or tributary, public improvements. The land use or development, its users and the public, should receive legitimate benefits from the construction of new or upgraded public facilities."
    }
  ],
  "Chapter 27.08 RULES OF PROCEDURE": [
    {
      "heading": "27.08.010 PLANNING APPLICATION SUBMITTAL.",
      "id": "/us/ca/cities/san-mateo/code/27.08.010",
      "text": "(a) A planning application (PA) shall be submitted for any project requiring a: (1) Site plan and architectural review; (2) Special use permit; (3) Temporary use permit; (4) Variance; (5) Site development permit; (6) Subdivisions; (7) Reclassification; (8) Planned development; (9) General Plan amendment; (10) Specific plan amendment; or (11) Code amendments regarding land use regulation. (12) Downtown Economic Development Permit. (13) Planned signing districts and freestanding signs over 8 feet in commercial districts. (14) Single Family Dwelling Design Review (SFDDR). (b) A planning application shall be filed on the form prescribed by the Department of Community Development, and shall include such information as may be required. The contents of the application and any reports pertaining thereto shall make up the official file. Each submitted application shall receive a PA number. (c) Each application shall be accompanied by: (1) A written statement by the owner(s) of the property approving submittal of the complete application; in instances where the applicant is not the same person as the owner, a statement signed by the owner (a) describing the nature of the applicant's interest, and (b) authorizing the applicant to act on behalf of and to bind the owners, shall also be required. (2) An accurate legal description of the property; (3) A scaled map or diagram of the property; (4) A statement describing the existing improvements on and use of the subject property and any proposed changes; (5) Fees or deposits set by Council resolution pursuant to Chapter 27.12; (6) Other documents or information that may be required including, but not limited to: Title reports; dimensioned architectural drawings showing elevations of existing and proposed buildings; existing and proposed landscaping and other ground treatment; required parking facilities; building and development data; sign information; photographs; materials sample boards; scale models; photomontages, or environmental information. (7) For properties subject to Single Family Dwelling Design Review (SFDDR), a statement under penalty of perjury, along with a proof of service, that the applicant has noticed the owners of properties within a 500-foot radius of the boundaries of the property that is the subject of the application as such owners are shown on the most recent San Mateo County assessor's property tax roll available at the San Mateo City Hall, has provided opportunity for discussion of the proposed application with the owners, and has allowed available plans to be reviewed by them. (d) Applications shall be set for review when determined by the Zoning Administrator to be complete. (e) Planning applications may consist of single or multiple development approval requests. Environmental documents shall be filed in conjunction with other approval requests, except that applicants may also request that a Master Environmental Assessment or Master Environmental Impact Report be prepared and approved prior to approval of a project. (f) Planning applications also include formal actions which are final with the Zoning Administrator."
    },
    {
      "heading": "27.08.020 RECLASSIFICATION AND CODE AMENDMENTS REGARDING LAND USE REGULATION.",
      "id": "/us/ca/cities/san-mateo/code/27.08.020",
      "text": "A reclassification of property or changes in zoning regulations may be initiated by the City Council, the Planning Commission, the Zoning Administrator, by property owners in the case of property reclassifications or by the general public for zoning regulation changes. Upon City Council approval, an application for a reclassification of four or more parcels may be made without fee by owners of fifty percent or more of all property within an area to be reclassified, where a potential public benefit of such reclassification can be demonstrated. When the Council makes a reclassification contingent upon receipt of a required permit and that permit is not obtained, the change in zone on the property which had been the subject of the reclassification shall not take effect."
    },
    {
      "heading": "27.08.030 SITE PLAN AND ARCHITECTURAL REVIEW (SPAR).",
      "id": "/us/ca/cities/san-mateo/code/27.08.030",
      "text": "(a) The following projects, as well as other projects that may be designated in this code, require a site plan and architectural review and no such project shall commence until the approval body has approved a planning application for site plan and architectural review: any building, new parking lot, fence over seven (7) feet in height, or an extension, alteration, or addition of or to an existing building or parking lot; historic buildings within the Downtown Specific Plan area as specified in Chapter 27.66. Single family and accessory buildings that conform to the standards contained in Chapter 27.18, or minor facade modifications as defined in Section 27.04.313, and which conform with Section 27.08.031, are exempt from this requirement, unless they are specifically designated by this section as requiring review. In making its review, the Zoning Administrator, Development Review Board, and Planning Commission shall be guided by the standards adopted by the Planning Commission and City Council. The application shall be approved if the Zoning Administrator or Commission finds all of the following to exist: (1) The structures, site plan, and landscaping are in scale and harmonious with the character of the neighborhood; (2) The development will not be detrimental to the harmonious and orderly growth of the City; (3) The development will not impair the desirability of investment or occupation in the vicinity, and otherwise is in the best interests of the public health, safety, or welfare; (4) The development meets all applicable standards as adopted by the Planning Commission and City Council, conforms with the General Plan, and will correct any violations of the zoning ordinance, building code, or other municipal codes that exist on the site; (5) The development will not adversely affect matters regarding police protection, crime prevention, and security. (b) All buildings, structures, landscaping, and other establishments shall be constructed in accordance with the approved drawings. (c) The City Council shall review and make the final determination on all buildings exceeding fifty-five (55) feet in height or where required by express General Plan provisions."
    },
    {
      "heading": "27.08.031 MINOR FACADE MODIFICATIONS—EXEMPTION FROM SITE PLAN AND ARCHITECTURAL REVIEW.",
      "id": "/us/ca/cities/san-mateo/code/27.08.031",
      "text": "Minor facade modifications shall be exempt from the requirements of a site plan and architectural review if the Zoning Administrator finds all of the following conditions to exist: (a) No building square footage or dwelling units are added; (b) The minor facade modification as a whole complements the architectural style of the building; (c) The various facade components, including but not limited to color, construction material and architectural features, are compatible and consistent with one another and complement the architectural style of the building; and (d) All other requirements of this Title are met. The Zoning Administrator may condition his or her /her decision by requiring such visual elements as may be necessary to make the above findings. Minor facade modifications not meeting the above conditions shall require submittal and approval of a Site Plan and Architectural Review application."
    },
    {
      "heading": "27.08.032 SINGLE FAMILY DWELLING DESIGN REVIEW (SFDDR).",
      "id": "/us/ca/cities/san-mateo/code/27.08.032",
      "text": "(a) Application Required. The following projects require a Single Family Dwelling Design Review (SFDDR) application and no such project shall commence prior to a final approved SFDDR application: (1) a new two-story residence in an R district; (2) a replacement single-family residence when a pre-existing single-family residence is to be substantially removed in any R district; (3) a second-story addition to an existing two-story residence in any R district of greater than 50 square feet; (4) an addition of any second-story square footage to an existing single story residence in an R district. (b) Small addition to an existing two-story residence. An addition to an existing two-story residence in an R district that does not exceed 200 square feet or 20% of the existing building square footage, whichever is less, shall be approved through the issuance of a building permit without further review if the following circumstances exist: (1) The project is consistent with the adopted Single Family Dwelling Design Guidelines; and (2) No appeal of the decision to issue a building permit is timely filed. (c) Application form and notice. SFDDR applications shall be filed on the form prescribed by the Department of Community Development, and shall include such information as may be required by the Department of Community Development. The SFDDR application may be filed only after a pre-application meeting between the applicant and the Department of Community Development Planning Division staff and after the applicant provides pre-application notification to the owners and tenants of property within 500 feet of the subject property and to neighborhood association(s) and the United Homeowners Association, in accordance with noticing procedures adopted by the Department. (d) Approval or denial. In making its review, Planning Division staff, the Zoning Administrator, Planning Commission, or City Council, as the case may be, shall be guided by the adopted R1 Single Family Dwelling Design Guidelines. The SFDDR application shall be approved if the decision-maker makes all of the following findings: (1) The structures, site plan, and landscaping are consistent with the adopted R1 Single Family Dwelling Design Guidelines; (2) The development will not be detrimental to the harmonious and orderly growth of the City; (3) The development will not impair the desirability of investment or occupation in the vicinity, and otherwise is in the best interests of the public health, safety, or welfare; (4) The development meets all applicable standards as adopted by the Planning Commission and City Council, conforms with the General Plan, and will correct any violations of the zoning ordinance, building code, or other municipal codes that exist on the site; (5) The development will not adversely affect matters regarding police protection, crime prevention, and security. (e) All buildings, structures, landscaping, and other improvements shall be constructed in accordance with the approved drawings. (f) Appeal. The Department of Community Development shall send notice of its intention to issue a building permit to persons entitled to notice of an application in accordance with Chapter 27.08 of this Code. An appeal may be filed in accordance with Chapter 27.08 of this Code no later than 10 calendar days after date of the decision."
    },
    {
      "heading": "27.08.035 COMPLETION OF PLANNING APPLICATION.",
      "id": "/us/ca/cities/san-mateo/code/27.08.035",
      "text": "(a) A planning application is determined to be complete when all documents, reports, data, maps, fees, and other information prescribed in Section 27.08.010 are submitted and are determined to be adequate to allow the approval body to determine if the required findings can be made. (b) The Zoning Administrator may require a new planning application for a project initially determined to be complete if one or more of the following occurs: (1) The project is significantly revised; (2) New information or material germane to the project is brought to light, or becomes available, or is required to assess a change, or revision in the proposed project and the information affects the ability of the approval body to make the required findings. (3) City policies, or standards are adopted which require substantial revisions in the project. If the Zoning Administrator finds that a new planning application is required, and no public hearing has been held on the project, then the application shall be considered withdrawn without prejudice. If a public hearing has been held, the approval body may accept the withdrawal with or without prejudice. Any unspent fees from the original application shall be applied to any new application or refunded, at the applicant's request. (c) The Zoning Administrator may close out an application, if information is requested in writing by the Zoning Administrator, and the information has not been submitted to the Zoning Administrator or the action has not occurred within 120 days. Files which are closed out are considered to be actions without prejudice, thereby enabling an immediate re-application for a project of the same, or similar nature by any applicant. The re-application shall be subject to all current fees and codes. (d) The Zoning Administrator's action may be appealed to the Planning Commission within ten (10) days of the Zoning Administrator's action closing out an application, or of determining that a new planning application is required."
    },
    {
      "heading": "27.08.040 PROCESSING OF APPLICATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.08.040",
      "text": "The Zoning Administrator shall make a decision on applications within the Zoning Administrator's authority or refer the application to the Planning Commission within twenty-one (21) days from the date the application is complete. Applications shall be set for public hearing by the Planning Commission within twenty-one (21) days from the date the application is complete and the environmental review process is completed. At this hearing all interested persons shall be heard. The Planning Commission may approve, conditionally approve, deny, or continue the application. Applications not final with the Commission, or final but appealed, shall be referred to an open agenda of the City Council, where all interested persons shall be heard. An approved application may be conditioned as may be deemed appropriate to further the purposes of the code."
    },
    {
      "heading": "27.08.045 CONDITIONS OF APPROVAL.",
      "id": "/us/ca/cities/san-mateo/code/27.08.045",
      "text": "(a) The approval of an application pursuant to this Title may be conditioned by the City in order to protect and preserve the health, safety, and welfare of the community and to secure the purposes of this Title. Unless otherwise provided, the conditions imposed shall run with the land and are binding on the successors, heirs, and assignees of the applicant. The City may require that any or all of the conditions imposed be recorded. (b) As a condition of approval of an application or otherwise, a property owner may create an easement for the benefit of the City, another governmental agency, or any other person for the purpose of ensuring ingress, egress, emergency access, light and air access, landscaping, parking, or open-space. A document creating such an easement shall comply with the requirements of Government Code Sections 65871 and 65873. (c) Any person may petition for the release of a condition or easement that has been recorded pursuant to this Section by filing an application for such a release with the Department of Community Development. An application for release of a recorded condition may be approved and a release recorded by the City if, after hearing, the Planning Commission determines that the condition is no longer reasonably related to the protection and preservation of the health, safety, and welfare of the community or the purposes of this Title. An application for release of a recorded easement may be approved and a release recorded if, after hearing, the Planning Commission determines that the easement is no longer necessary to accomplish the land use goals of the City. (d) Nothing contained in this Section shall be construed in any way to limit the City in its exercise of the powers the City derives from the State Constitution, State law, and the Charter, nor shall it be construed to supersede any provision of State or City law that requires additional procedural steps and decisions before an easement or right-of-way may be abandoned or vacated."
    },
    {
      "heading": "27.08.050 NOTICE OF APPLICATION.",
      "id": "/us/ca/cities/san-mateo/code/27.08.050",
      "text": "(a) Required Notice. All required notices shall be given by mail or e-mail to the applicant, appellant (if any), and all owners and tenants of property located within a radius of 500 to 1,000 feet of the property lines of the project site in accordance with procedures adopted by City Council resolution. Noticing shall be given to property owners as listed on the most recent San Mateo County Assessor's property tax roll available at the San Mateo City Hall. All notices shall include the date, time, and place of hearing, the name of the applicant, the purpose of the application, an identification of the subject property, and other facts as may be prescribed by the Planning Commission or City Council. Defects in such information, or the failure to give notice as fully as described, or the failure of any or all of the addressees to receive the notice shall not invalidate the proceedings, provided that the noticing has occurred in good faith. (b) Applicable notice periods. (1) Zoning Administrator. When the Zoning Administrator has final authority to act on an application, notice pursuant to this Section shall be mailed at least ten calendar days before a decision is reached by the Zoning Administrator, but no hearing shall be held. The Zoning Administrator shall indicate on the notice that any person may request in writing to be advised of the decision reached by the Zoning Administrator. (2) Planning Commission. Notices of public hearing shall be mailed at least ten calendar days prior to the first Commission hearing date. (3) City Council. Notice of public hearing shall be mailed at least ten calendar days prior to the first Council hearing date. (c) CEQA Notices. (1) Negative declaration. Notices regarding the availability of a project's negative declaration for public review shall be given at least 20 days prior to the hearing date of the Planning Commission. This notice may be combined with the Planning Commission public hearing notice described above. (2) Environmental Impact Report. Notices regarding the availability of a project's environmental impact report for public review shall be given when the notice of completion is filed, either 30 or 45 days prior to the expiration of the public comment period, depending upon the requirements of CEQA. (d) Posting of project site. As directed by the Chief of Planning or designee, applicants or their representatives shall place a public notice placard(s) on a highly visible portion of the project site which informs the public of any pending Zoning Administrator decision, Planning Commission study session or public hearing, or City Council public hearing pertaining to the planning application. The placard shall include the public hearing date, location, and purpose, including the permits requested by the applicant, a brief description of the project, and any other information required by the Chief of Planning or designee. The placard shall be posted at least ten days prior to any pending Zoning Administrator decision, Planning Commission study session or public hearing, or City Council hearing pertaining to the planning application. (e) Other notification. Notwithstanding the provisions above, notice by publication may be provided in lieu of, or in addition to, individual notice, when deemed warranted by time constraints, the number of notice recipients, or where otherwise required by law. In addition to other forms of notice, the Zoning Administrator may, at his or her discretion, give notice of an application by posting on or near the project site. (f) Public hearings regarding subdivisions. Pursuant to the Subdivision Map Act, in the case of all hearings on applications under Title 26 of this Code, notice shall be given by publication in a newspaper of general circulation in the City at least ten days prior to the hearing and posted in three public facilities at least ten days prior to the hearing, in addition to notice by mail. (g) Minutes. Minutes of the Planning Commission and City Council shall be available at the City Clerk's office when they are drafted and for a period of at least two weeks after the meeting or hearing. Actions by the Zoning Administrator shall be available at the City Clerk's office for a period of at least two weeks after the date of the action."
    },
    {
      "heading": "27.08.060 DECISIONS FINAL.",
      "id": "/us/ca/cities/san-mateo/code/27.08.060",
      "text": "(a) Approvals or Denials. Decisions on all applications on which the Zoning Administrator or the Planning Commission may take final action shall become effective ten (10) calendar days after the decision is made, unless an appeal is filed. Decisions of the City Council, unless otherwise stated, are effective and shall be final on the date Council action is taken. Reclassifications and projects requiring reclassifications or ordinance amendments shall, however, become effective on the effective date of the reclassification or other ordinance, or on the date of another event if prescribed in the reclassification or other ordinance. (b) Reapplications. New applications for the same planning project involving similar purposes shall not be accepted for review, if previously denied, for a period of one year from the date of the final action. However, the one-year limitation shall not apply if the final approval body (1) waives the limitation after an applicant's written request; or (2) states at the time of decision that the denial is without prejudice. (c) Covenants and Conditions. Unless otherwise provided, the decisions of the approval bodies shall run with the land. Conditions imposed by the approval bodies on a project are binding upon successors to the applicant."
    },
    {
      "heading": "27.08.080 PLANNING APPLICATION MODIFICATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.08.080",
      "text": "An applicant may request modifications to a previously approved planning application prior to or during construction. Examples of such modifications include alteration to an approved building or structure, change in configuration of site improvements, or modification or deletion of conditions of approval. For previously approved Special Use Permits, an applicant may also request a change of use after a project has been completed. A modification shall not automatically extend the approval expiration date beyond that of the original planning application. Modifications are classified in three ways based on the significance of the proposed change and amount of additional review required: (a) substantial conformance, (b) minor, or (c) major. The Zoning Administrator shall determine the type of modification required based on the criteria specified below. This decision shall be final. (a) Substantial Conformance. Modifications that are in substantial conformance with the original planning application can be approved as part of the building permit review process. (1) Substantial conformance is generally defined as a modification or change that: (A) Results in a project with reduced or inconsequential changes in size, scale, design, or intensity; or (B) Is necessary to accommodate parking requirements, utility configurations or other mechanical or operational components of a project identified during building permit review or construction; or (C) Cumulatively would not result in substantive changes to the overall project. (2) Public notification shall not be required for substantial conformance modifications. (b) Minor Modification. Modifications that result in minor changes to an approved planning application require review and approval by the Zoning Administrator. (1) Minor modification is generally defined as a modification where all of the following circumstances apply: (A) The modification would not result in a Major Modification, as defined below, to the approved site plan or project design; and (B) The modification would not significantly change the nature of the approved use(s); and (C) The modification would not significantly intensify the approved use(s); and (D) The modification would not result in any new or substantially greater environmental effects than the originally approved project. (2) Public notification to adjacent property owners and occupants is required for a minor modification. The Zoning Administrator shall determine whether additional property owners and occupants shall be notified depending on the nature of the modification, consistent with the notification procedures in Chapter 27.08. (c) Major Modification. Modifications that result in a significant change require review and approval by the decision making body under Chapter 27.06. (1) A modification to a project is considered major if any of the following circumstances apply: (A) The modifications involve substantive changes to the approved site plan or project design. A substantive change, for the purpose of this section, includes but is not limited to: (i) A change that is visually conspicuous from the public right-of-way or adjacent properties; or (ii) A change that results in non-conformance with City standards or policies in order to comply with updated Federal or State laws including. but not limited to, the Americans with Disability Act, Building Code requirements, or Fire Code requirements; or (iii) A change that alters the intent of a project-specific condition of approval. (B) The modifications significantly change the nature of the approved use; or (C) The modifications significantly intensify the approved use; or (D) The modifications may result in new or substantially greater environmental impacts than the originally approved project; or (E) The modifications involve major policy decisions or unique land use characteristics, as determined by the Zoning Administrator. (2) Public notification is required when approval by the Zoning Administrator is required, pursuant to Chapter 27.08. If the original decision maker was the Planning Commission or City Council, whether in the first instance or on appeal, then public noticing and public hearing for approval by the Planning Commission are required. All recipients and interested parties of the previously approved planning application shall be notified."
    },
    {
      "heading": "27.08.085 PLANNING APPROVAL EXPIRATION.",
      "id": "/us/ca/cities/san-mateo/code/27.08.085",
      "text": "Final approval of a planning application shall expire two years from the date of approval, with the following exceptions: (a) A completed building permit application is filed before the expiration date and a building permit is issued prior to or within six months after the two year expiration date. (b) The property within two years has been used in conformance with the final order. (c) Approvals granted to the City of San Mateo or the Redevelopment Agency of San Mateo shall be in force and effect for such time period as funds are budgeted in whole or in part for the project by the City or Agency. (d) Projects with associated subdivision maps that remain in effect or have been extended by mandate of the state Subdivision Map Act or San Mateo Municipal Code section 26.48.135, 26.48.140, or 26.56.087. Those planning approvals remain effective for the term of the subdivision map approval, if required by State law. (e) Projects for which an extension has been obtained in accordance with Section 27.08.087 below."
    },
    {
      "heading": "27.08.087 PLANNING APPROVAL EXTENSION.",
      "id": "/us/ca/cities/san-mateo/code/27.08.087",
      "text": "The following extensions to planning approvals are available: (a) Extensions required by state or federal law. Where state or federal law requires that extension of a planning approval be considered, the Zoning Administrator shall approve an extension if they find that the project complies with all applicable zoning, planning, and general plan regulations and conditions. (b) City extensions. The Zoning Administrator may approve one extension of a planning approval for up to two years, subject to the following provisions: (1) Application required. To apply for a planning approval extension, an applicant must submit the application prior to the expiration date of the planning approval, pay the application fee and provide the reason(s) for the extension request. (2) Findings required. To approve a time extension, the Zoning Administrator must find all of the following: (A) The approved project is still consistent with the City's General Plan; and (B) The approved project is still consistent with the City's Zoning Ordinance; and (C) The extension will not result in any new environmental impacts or an increase in severity of previously identified environmental impacts. (c) Notice of Zoning Administrator Decision on Extension. Notice will be provided to the neighborhood by the same process followed for the original project approval. Notice will also be provided to the Planning Commission and City Council within ten days of the Zoning Administrator's decision. (d) Appeals. The decision of the Zoning Administrator is appealable to the Planning Commission within ten days of the Zoning Administrator's decision by filing a written appeal with the Planning Division and payment of applicable fees. When an appeal is filed, the expiration date of a planning approval is tolled until a final action is taken. The provisions of Municipal Code Chapter 26.48 govern for all projects with associated subdivision maps."
    },
    {
      "heading": "27.08.090 APPEALS.",
      "id": "/us/ca/cities/san-mateo/code/27.08.090",
      "text": "All appeals must be filed prior to the effective date of a decision, in writing, and be accompanied by payment of the filing fee. If an application has been denied by an approval body, only the applicant may appeal the denial. If an application or a portion thereof is approved, an appeal may be made by the applicant, any interested citizen or taxpayer. When an appeal is properly filed, the application shall be set for hearing on an open agenda of the approval body to whom the appeal is authorized. All documents, plans, and papers constituting the record of the action from which an appeal is taken shall be forwarded to the approval body hearing the appeal and shall be considered part of the record of the de novo (new) hearing. (a) Appeals to the Planning Commission. Appeals shall be filed with the Commission through the office of the Zoning Administrator. (b) Appeals to the City Council. Appeals shall be filed with the City Clerk, who shall forward one copy to the Commission through the office of the Zoning Administrator. Decisions by the Zoning Administrator shall be reviewed by the Commission if a member of either the Commission or the Council files a written request with the Commission through the office of the Zoning Administrator. Decisions of the Commission shall be reviewed by the Council if a Council member files a written request with the City Clerk. No fees are required when a Commissioner or Council member requests review of an application."
    },
    {
      "heading": "27.08.100 WITHDRAWAL OF APPLICATION.",
      "id": "/us/ca/cities/san-mateo/code/27.08.100",
      "text": "An applicant may withdraw an application at any time by filing a written notice of withdrawal with the appropriate approval body. If an application is withdrawn prior to any public hearing on the project, the withdrawal is without prejudice, and the application may be resubmitted at any time. If an application is withdrawn after a public hearing on the project, the applicant and all other persons are prohibited for a period of 1 year from the date of withdrawal from filing a new application for the same, or substantially the same purpose. A previously withdrawn application may be resubmitted prior to the expiration of the waiting period if (a) the final approval body specifies that such withdrawal is without prejudice, or (b) the withdrawal is made pursuant to Section 27.08.035(b) prior to any public hearing on the project."
    },
    {
      "heading": "27.08.110 ENTRY OF FINAL ORDERS.",
      "id": "/us/ca/cities/san-mateo/code/27.08.110",
      "text": "The City Clerk shall enter all final orders made by the Commission and the Council on all applications and appeals under this Title in the appropriate records therefor, in such a manner as to identify the applicant, the property, the use, and the action ordered. The Zoning Administrator shall enter all final orders made by the Planning Commission on all applications under this Title in the appropriate records therefor, in such a manner as to identify the applicant, the property, the uses, and the action ordered."
    }
  ],
  "Chapter 27.10 REVIEW PROCEDURE": [
    {
      "heading": "27.10.010 REVOCATION OF PLANNING APPROVALS.",
      "id": "/us/ca/cities/san-mateo/code/27.10.010",
      "text": "In addition to any other remedies established by the Code, in the event any person utilizing a planning application approval violates its terms or fails to comply with its conditions, or violates the provisions of this code in effect at the time approval was granted, or directly or indirectly conducts, carries on, or allows to be conducted or carried on such violations, the Planning Commission shall have the power to permanently revoke or suspend the planning application approval as hereinafter provided."
    },
    {
      "heading": "27.10.020 REVOCATION PROCEDURES.",
      "id": "/us/ca/cities/san-mateo/code/27.10.020",
      "text": "(a) No planning application approval shall be permanently revoked or suspended until a hearing is held by the Planning Commission. Written notice of such hearing shall be served upon the property owner, applicant, and occupant of the premises either personally or by certified mail. Notice shall be given to all property owners within a three-hundred-foot radius of the exterior boundaries of the subject property in the manner provided in Section 27.08.050. Such notice shall be given at least ten calendar days prior to the date set for hearing and shall state: (1) The alleged violation(s); (2) The date, time and place the hearing is to be held. (b) At the hearing the property owner, applicant, and occupant shall be given the opportunity to be heard in person or through their representative(s), and may call witnesses and present evidence on their behalf. Additionally, the commission may hear such other testimony as it deems appropriate. (c) Upon the conclusion of the hearing, the commission shall determine whether or not the approval shall be suspended, revoked, modified or left unaltered. The commission shall be authorized to grant time to correct the violation(s). Any person may appeal the action of the commission to the City Council in accord with the provisions of Section 27.08.070. Notice of the hearing before the Council shall be given in the manner provided in this section for hearings before the commission. (d) In any case where a planning application approval is revoked, no new approval may be granted to any person to conduct or carry on the same or similar activity on the subject property until all conditions of the approval are met."
    },
    {
      "heading": "27.10.030 APPLICATIONS FOR BUILDING PERMITS AND BUSINESS PERMITS.",
      "id": "/us/ca/cities/san-mateo/code/27.10.030",
      "text": "The zoning administrator shall review all applications for building permits and business permits and business tax return names and addresses to determine whether a proposed building or structure, or use, or business is in compliance with this title. No building permit shall be issued authorizing work upon property for which a planning application is being processed unless such work is unrelated to the planning application and/or a delay in work poses an immediate threat to the health and safety of the premises or the occupants thereof. No building permit or business permit shall be issued until the zoning administrator shall have approved such application by stamping or affixing his or her written approval on such application."
    },
    {
      "heading": "27.10.035 APPLICATIONS FOR DEMOLITION PERMITS.",
      "id": "/us/ca/cities/san-mateo/code/27.10.035",
      "text": "Demolition permits shall not be issued unless the requirements set forth in Section 23.06.035 are met."
    },
    {
      "heading": "27.10.040 CERTIFICATE OF OCCUPANCY APPROVAL.",
      "id": "/us/ca/cities/san-mateo/code/27.10.040",
      "text": "No new building for which a planning application is required may be occupied after completion of its construction, alteration, or addition until the certificate of occupancy to be issued by the building official is approved in writing by the zoning administrator or designee."
    }
  ],
  "Chapter 27.12 FEES": [
    {
      "heading": "27.12.010 FEES—APPLICATIONS OR APPEALS.",
      "id": "/us/ca/cities/san-mateo/code/27.12.010",
      "text": "For the purpose of reimbursement of the City for the administration of this title, the Council shall, by resolution from time to time, fix the amount of fees to be charged for processing all applications and appeals provided for in this title. Said resolution may contain provisions for refunds where applications have been withdrawn."
    }
  ],
  "Chapter 27.13 TRANSPORTATION IMPROVEMENT FEE": [
    {
      "heading": "27.13.010 AUTHORITY.",
      "id": "/us/ca/cities/san-mateo/code/27.13.010",
      "text": "This chapter is enacted pursuant to Government Code §§66000-66009 and to the Charter City authority provided by the Constitution of the State of California."
    },
    {
      "heading": "27.13.020 APPLICATION.",
      "id": "/us/ca/cities/san-mateo/code/27.13.020",
      "text": "This chapter applies to fees charged as a condition of development approval to defray the cost of certain transportation improvements required to serve new development within the City of San Mateo. This chapter does not replace normal subdivision map exactions or other measures required to mitigate site specific impacts of a development project including but not limited to, mitigations pursuant to the California Environmental Quality Act; regulatory and processing fees; fees required pursuant to a development agreement; funds collected pursuant to a reimbursement agreement that exceed the developer's share of public improvement costs; or assessment district proceedings, benefit assessments, or taxes."
    },
    {
      "heading": "27.13.030 INTENT AND PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.13.030",
      "text": "The City Council of the City of San Mateo declares that: (a) Adequate transportation improvements are needed to protect the health, safety, and general welfare of the citizens to facilitate transportation, and to promote economic well-being within the City; (b) The City of San Mateo provides transportation improvements and services for residents, businesses, and employees within the City; (c) Individual transportation improvements are part of an integrated system serving and providing benefits to the entire City; (d) The Level of Service \"D\" (Average Delay of 45 seconds) shall be the interim standard for all street and intersection improvements pending adoption of the revised General Plan. (e) New development within the City will create an additional burden on the existing transportation system; (f) Improvements to the existing transportation system in the City are needed to mitigate the cumulative impacts of new development and to accommodate future development by maintaining Level of Service \"D\" on all streets and intersections; (g) All types of urban development require and use the transportation system; (h) There are not adequate public funds available to maintain Level of Service \"D\" at all intersections in the City. (i) In order to ensure that Level of Service \"D\" is maintained, and to promote the health, safety, and general welfare of the community, it is necessary that new development pay a fee representing its share of costs of the necessary improvements; (j) The transportation improvement fee is based upon the evidence that new development generates additional residents, employees, and structures which in turn place an additional cumulative burden upon the local transportation system and should be expected to pay a share of the new facilities. (k) The purpose of this fee is to help provide adequate transportation improvements to serve cumulative development within the City. However, the fee does not replace the need for all site-specific transportation improvements that may be needed to mitigate the impact of specific projects upon the City's transportation system. (l) The transportation improvements for which the fee will be used are identified in the City's Capital Improvements Program (CIP) and/or in the Transportation Improvement Fee Technical Report."
    },
    {
      "heading": "27.13.040 DEFINITIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.13.040",
      "text": "The following definitions apply to this chapter: (a) \"Transportation Improvements\" includes all street and intersection improvements and related facilities and equipment. (b) Level of Service \"D\" means an average delay for a given street segment or intersection of 0.45 seconds or better. (c) Land use categories are defined as follows: (1) Hotel, which includes facilities used for the overnight lodging of guests. (2) Industrial, which includes but is not limited to, facilities used for the manufacturing, processing, or storage of goods. (3) Institution, which includes but is not limited to, religious, governmental, educational, and cultural uses. (4) Multi-family residential, which includes but is not limited to, a secondary unit, duplex, townhouse, apartment, condominium, mobile home, multiple family dwelling, and community care facility with more than six residents. (5) Office, which includes but is not limited to, facilities primarily used for professional (legal, engineering, accounting), financial, insurance, real estate, and other office-related uses which do not provide primarily walk-in services to the public. (6) Retail, which includes but is not limited to, facilities primarily used for the sale of retail goods or personal services, including all retail sales outlets, facilities for the on-site sale of food or beverages, and personal services such as laundries, cleaners, copy stores, and hairdressers. (7) Single Family Residential, which includes but is not limited to, a single-family dwelling and a small community care facility with six or fewer residents. (8) Other uses. The zoning administrator shall determine the appropriate land use category for any use not set forth above, based on similarity of use and peak hour trip characteristics of the use as indicated in the most current edition of the International Transportation Engineering Manual."
    },
    {
      "heading": "27.13.050 FEE REQUIREMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.13.050",
      "text": "(a) General. The amount of the proposed fee shall be established by resolution of the City Council and shall be based upon the following considerations: (1) Development will pay only for improvements where there is a reasonable relationship between the road improvements and the traffic generated by the new development. (2) Each type of development shall contribute to the needed improvements in proportion to the use of improvements by that type of development. (b) Types of Development Subject to the Fee. The fee shall be applicable to new development projects which require a planning application pursuant to Section 27.08.010, expansion of floor area of existing uses which require a planning application pursuant to Section 27.08.010, new single family and duplex dwelling units, and changes of use requiring a special use permit as follows: (1) Residential construction. Fees shall be charged for each new dwelling unit. No fee is applicable for remodeling or for an addition to an existing unit not resulting in a new unit. (2) Non-residential construction. Fees shall be charged on a per square foot basis for all new gross floor area, including additions where floor area is increased. No fee is applicable for remodeling or restoration only, where the floor area is improved or replaced but not increased. Gross floor area is determined in accordance with Section 27.04.200 of this code, except for Subsection 27.04.200(b)(1), which shall not apply. Floor area measurement shall be to the exterior facade of building wall planes or from center line of party walls. Parking area and exterior walkways are not included in the fee calculation. (3) Changes of use requiring a special use permit. Fees shall be charged upon the incremental difference between the fee calculated for the floor area of a prior legal use and the fee calculated for the floor area of the proposed new use. (c) Land Use Categories Subject to the Fee. All land use categories which generate traffic are subject to the fee. Specific land use categories are defined in Section 27.13.040. (d) Improvements Funded. The fee shall be based on the percentage of the cost of the new improvements attributable to new development as determined in the Transportation Impact Fee Technical Report, dated June 1990 prepared by Economic and Planning Systems Inc. (EPS), and future additions and amendments to said report, all of which are incorporated in this chapter by this reference. (e) Formula. The amount of the fee shall be determined by the following formula: Fee = Average Peak Hour Trips per Land Use Unit x Average Cost per Trip x Number of Land Use Units in Subject Application Land Use Unit means dwelling units for residential uses, or square foot for non-residential uses. Average Trips per Land Use Unit is the number of evening peak hour trips per Land Use unit for each category of land use as determined by the Transportation Improvement Fee Technical Report. Average Cost per Trip is the estimated transportation improvement costs attributable to new development within the City divided by the number of new evening peak hour trips associated with new development as determined in the Transportation Improvement Fee Technical Report or subsequent amendments to the Technical Report. Number of Land Use Units is the total number of residential dwellings or non-residential square feet involved in the project subject to the fee. (f) The zoning administrator shall have authority to render final determinations regarding the appropriate classification of land use and the correct calculation of gross building floor area for a particular development project."
    },
    {
      "heading": "27.13.060 FEE PAYMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.13.060",
      "text": "The Transportation Improvement Fee shall be paid in full to the City of San Mateo before the first building permit is issued, or if the building permits are phased, at issuance of the superstructure permit. If no building permit is required, the fee shall be paid before a conversion of use may take place. The fee shall not apply to any project submitted for a building permit as of the date of introduction of this ordinance."
    },
    {
      "heading": "27.13.070 AUTHORITY FOR ADDITIONAL MITIGATION.",
      "id": "/us/ca/cities/san-mateo/code/27.13.070",
      "text": "Fees collected pursuant to this chapter are not intended to replace or limit requirements to provide mitigation of traffic impacts not mitigated by the Traffic Improvement Fee and created by a specific project, and imposed upon development projects as part of the development review process."
    },
    {
      "heading": "27.13.080 EXEMPTIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.13.080",
      "text": "Public park facilities, City buildings, and those public facilities entitled to an exemption under law, are exempt from the Transportation Improvement Fee."
    },
    {
      "heading": "27.13.090 FEE CREDIT.",
      "id": "/us/ca/cities/san-mateo/code/27.13.090",
      "text": "(a) The Community Development Director and Public Works Director may adjust the fee imposed pursuant to this chapter in consideration for certain on-site and off-site facilities or improvements constructed or paid for by the developer. A developer is entitled to credit for the value of improvements if the improvement is identified in the Transportation Improvement Fee Technical Report and the developer: (1) dedicates land for the improvement(s) identified in the Technical Report, (2) constructs the improvement(s), (3) finances the improvement(s) by cash, pays the assessments of an assessment district, or Mello-Roos Community Facilities District, or (4) a combination of the above."
    },
    {
      "heading": "27.13.100 APPEAL.",
      "id": "/us/ca/cities/san-mateo/code/27.13.100",
      "text": "The developer of a project subject to this chapter may appeal the imposition and/or calculation of the fee. (a) The appeal shall be processed in accordance with Section 27.08.090 of this code. An appeal by a developer of a project not requiring a planning application, shall be to the zoning administrator. (b) Notice of the appeal shall be provided in accordance with applicable provisions in Section 27.08.050 of this code. (c) The appellant shall state in detail the factual basis for the appeal and shall bear the burden of proof in presenting substantial evidence to support the appeal. (d) The appeal body shall uphold the fee and deny the appeal if it finds that there is a reasonable relationship between the development project's impact on transportation facilities and the amount of the fee. The appeal body shall consider the land use category determination, and the substance and nature of the evidence, including the fee calculation method, supporting technical documentation, and the appellant's technical data. Based on the evidence, the appeal body may also modify the fee."
    },
    {
      "heading": "27.13.110 REFUND OF FEE.",
      "id": "/us/ca/cities/san-mateo/code/27.13.110",
      "text": "(a) If a building permit or use permit expires, is canceled, or is voided and any fees paid pursuant to this chapter have not been expended, no construction has taken place, and the use has never occupied the site, the Director of Public Works may, upon the written request of the applicant, order return of the fee and interest earned on it, less administrative costs. (b) During the annual review pursuant to Section 27.13.120, the City Council shall make a finding with respect to any fee revenue not expended or committed 5 years or more after it was paid. If the City Council finds that the fee revenue is not committed, it shall authorize a refund to the then owner of the property for which the fee was paid, pursuant to Government Code §66001 or successor legislation."
    },
    {
      "heading": "27.13.120 ACCUMULATION AND USE OF FUNDS.",
      "id": "/us/ca/cities/san-mateo/code/27.13.120",
      "text": "(a) Transportation Improvement Fee Fund. The City shall deposit the fees collected under this chapter in a special fund, the Transportation Improvement Fee Fund, designated solely for transportation improvements. (b) Use of Funds. The fees and interest earned on accumulated funds shall be used only to: (1) Complete the transportation improvement projects specified in the Transportation Improvement Fee Technical Report, or to reimburse the City for such construction if funds were advanced by the City from other sources; or (2) Reimburse developers who have been required or permitted to install improvements identified in the Transportation Improvement Fee Technical Report which are oversized in width, length, or capacity, relative to demand generated by the subject project; or (3) Pay costs required for the administration of this ordinance."
    },
    {
      "heading": "27.13.130 ANNUAL REVIEW.",
      "id": "/us/ca/cities/san-mateo/code/27.13.130",
      "text": "The Transportation Improvement Fee authorized by this chapter, implementing Council Resolutions, and supporting documentation, including the Transportation Improvement Fee Technical Report, shall be reviewed annually by the City Council in order to make any findings required by State law."
    }
  ],
  "Chapter 27.14 REDEVELOPMENT": [
    {
      "heading": "27.14.010 RELOCATION ASSISTANCE.",
      "id": "/us/ca/cities/san-mateo/code/27.14.010",
      "text": "The following requirement for relocation assistance payments shall be applied to applicants within the downtown redevelopment project area: (a) Relocation assistance payments shall be made to low and moderate income households within the downtown redevelopment project area who are displaced after having received a notice to vacate or a rent increase rendering their unit not affordable, such notice or increase being within 90 days of the filing of an application to proceed with (1) the demolition of residential units; (2) the rehabilitation of residential units when such rehabilitation exceeds 25% of the market value of the unit as determined by the building official; (3) the conversion of residential units into non-residential units; or (4) the conversion of rental units into owner occupied units. (b) Relocation assistance payments shall be made to low and moderate income households within the downtown redevelopment project area who are displaced after having received a notice to vacate or a rent increase rendering their unit not affordable, such notice or increase being subsequent to the filing of an application to proceed with the activities listed as subsections (a)(1)—(4) of this section; provided, however, that such displacement occurs within one year of completion of the development for which the application is filed."
    },
    {
      "heading": "27.14.020 CONDITIONS FOR RELOCATION ASSISTANCE.",
      "id": "/us/ca/cities/san-mateo/code/27.14.020",
      "text": "The relocation assistance payments set forth in Section 27.14.010 shall be subject to the following terms and conditions: (a) The eligibility requirements set forth in government code Sections 7260 et seq. for \"displaced persons,\" including such regulations for eligibility adopted pursuant to said section, shall be applicable to households seeking relocation assistance payments. (b) The total relocation assistance payment shall be the equivalent of three months rent being paid by the displaced household immediately prior to displacement. (c) No household or persons who comprise or comprised that household shall receive relocation payments more than once in every two years and in no event more than twice during the life of the redevelopment project. To be eligible a household or persons must be in lawful possession of an affordable residential unit at the time that said unit is rendered unaffordable by an activity designated in Section 27.14.010(a)(1)—(4) or at the time that a notice to vacate is received in order to proceed with an activity designated in Section 27.14.010(a)(1)—(4). (d) Not more than one relocation payment during the life of the redevelopment project shall be made for each residential unit regardless of the number of times that displacement occurs from such individual unit. (e) Complaints may be brought by persons of low or moderate income households who have been denied relocation assistance payments to the Community Relations Commission by filing a written complaint not later than 18 months after displacement or the claim is forfeited."
    },
    {
      "heading": "27.14.030 APPLICATION FOR DEVELOPMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.14.030",
      "text": "At the time of application for a permit to proceed with an activity listed in Section 27.14.010(a)(1)—(4) applicant shall submit a certified list of his or her residential tenants along with the monthly rent being paid for each respective residential unit. Applicant shall also specify any rental changes that were implemented within 90 days prior to the date of application."
    },
    {
      "heading": "27.14.040 NOTICE.",
      "id": "/us/ca/cities/san-mateo/code/27.14.040",
      "text": "City shall send notice to each residential tenant. Said notice shall indicate that an application has been filed and that relocation benefits may be available."
    },
    {
      "heading": "27.14.050 SECURITY.",
      "id": "/us/ca/cities/san-mateo/code/27.14.050",
      "text": "No permit shall be issued until the applicant posts security to assure that relocation assistance payments will be made. Said security shall be a performance bond, letter of credit, certificate of deposit, or the like in an amount equal to the total relocation assistance payments anticipated. Applicant may apply for a total or partial release of said security when payments have been made to at least 50% of eligible tenants."
    },
    {
      "heading": "27.14.060 MAKING OF PAYMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.14.060",
      "text": "Payments required by this chapter shall be made by the applicant. Payments may be a condition of permit approval."
    },
    {
      "heading": "27.14.070 ELIGIBLE TENANTS.",
      "id": "/us/ca/cities/san-mateo/code/27.14.070",
      "text": "The City, acting through its Department of Community Development, Housing and Economic Development Division, may investigate the eligibility of particular tenants for relocation assistance."
    },
    {
      "heading": "27.14.080 DEFINITIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.14.080",
      "text": "The following definitions apply to this section: \"Affordable\" shall be defined as set forth in Health and Safety Codes Sections 50052.5 and 50053 or such successor sections. \"Applicant\" shall mean any person, entity, corporation, partnership, or otherwise, but shall not include the City of San Mateo and the San Mateo Redevelopment Agency and other governmental entities. \"Application\" shall include planning, subdivision, and building applications where the context is appropriate; provided, however, that the requirement to provide relocation assistance payments shall attach to the first of such required applications. \"Life of the Redevelopment Project\" shall mean through July 7, 2011, or such earlier date if the project is sooner terminated. \"Low and moderate income households\" shall be defined as set forth in Health and Safety Code Sections 50093 and 50l05 or such successor sections."
    }
  ],
  "Chapter 27.15 DENSITY BONUS": [
    {
      "heading": "27.15.010 Purpose.",
      "id": "/us/ca/cities/san-mateo/code/27.15.010",
      "text": "The purpose of this section is to comply with the state density bonus law (California Government Code section 65915) and to implement the housing element of the San Mateo General Plan, by providing increased residential densities for projects that guarantee that a portion of the housing units will be affordable to very low, low, or moderate-income households, provide senior citizen housing, or include child care facilities."
    },
    {
      "heading": "27.15.020 Applicability.",
      "id": "/us/ca/cities/san-mateo/code/27.15.020",
      "text": "The provisions of this section apply to the construction of five or more housing units that satisfy one or more of the following criteria: (a) At least ten percent of the total units are designated for low income households. (b) At least five percent of the total units are designated for very low income households. (c) A senior citizen housing development as defined in Section 51.3 of the Civil Code. (d) At least ten percent of the total units in a condominium project as defined in subdivision (e) of, or in a planned development as defined in subdivision (k) of, Section 1351 of the Civil Code, are designated for moderate income households, provided that all units in the development are offered to the public for purchase."
    },
    {
      "heading": "27.15.030 Definitions.",
      "id": "/us/ca/cities/san-mateo/code/27.15.030",
      "text": "The following terms are defined for purpose of this section: (a) \"Density bonus\" means a density increase, in the amount prescribed by Government Code section 65915, over the otherwise maximum allowable residential density as of the date the application is accepted as complete. (b) \"Low income household\" has the meaning set forth in Health and Safety Code section 50079.5 and is a household whose income is equal to or less than eighty percent of the area median income, as published by the California Department of Housing and Community Development. (c) \"Moderate income household\" has the meaning set forth in Health and Safety Code section 50093 and is a household whose income is equal to or less than one hundred twenty percent of the area median income, as published by the California Department of Housing and Community Development. (d) \"Senior citizens\" means qualifying residents as defined in Section 51.3 of the Civil Code. (e) \"Very low income household\" has the meaning set forth in Health and Safety Code section 50105 and means a household whose income is equal to or less than fifty percent of the area median income, as published by the California Department of Housing and Community Development."
    },
    {
      "heading": "27.15.040 Incentives and Concessions.",
      "id": "/us/ca/cities/san-mateo/code/27.15.040",
      "text": "(a) City to grant. When an applicant qualifies for a density bonus as prescribed by Government Code section 65915, the City will grant the number of incentives or concessions required by that section unless it makes one of the following findings: (1) The concession or incentive does not result in identifiable and actual cost reductions to provide for affordable housing costs, as defined in Section 50052.3 of the Health and Safety Code, or for rents for the targeted units to be set as specified in Section 65915(c) of the Government Code. (2) The concession or incentive would have a specific adverse impact, as defined in Government Code Section 65589.5 (d)(2), upon public health and safety or the physical environment or on any real property that is listed in the California Register of Historical Resources and there is no feasible method to satisfactorily mitigate or avoid the specific adverse impact without rendering the development unaffordable to low- and moderate-income households. (3) The concession or incentive would be contrary to state or federal law. (b) The following incentives and concessions are deemed not to have the adverse impact set forth in section (a)(2) above: (1) Reduced setbacks or buffers so long as the project remains consistent with the City's General Plan and any applicable design guidelines; (2) Increased maximum lot coverage so long as the project remains consistent with the City's General Plan and any applicable design guidelines; (3) Increased maximum Floor Area Ratio so long as the project remains consistent with the City's General Plan and any applicable design guidelines; (4) Reduction in parking standards for residential units beyond that set forth in Government Code section 65915(p); and (5) In addition to the additional density bonus provided in accordance with Government Code section 65915(g) for land donations within ¼ mile of an applicant's project, provision of the additional density bonus set forth in Government Code section 65915(g) for land dedicated to the City that is located within ½ mile of the applicant's project so long as the applicant demonstrates to the City's satisfaction that building the requisite number of affordable units on-site is infeasible and there is an identified source of funding for the very low income units. (c) The City will not, however, provide any direct financial assistance, waive fees or dedication requirements, or provide publicly owned land for a housing development as an incentive or concession."
    },
    {
      "heading": "27.15.050 Waivers and Modifications of Development Standards.",
      "id": "/us/ca/cities/san-mateo/code/27.15.050",
      "text": "(a) Proposal. In accordance with Government Code section 65915(e), an applicant may propose waiver or modification of development standards if they would physically preclude the construction of a development meeting the criteria of section 65915(b) at the densities or with the concessions or incentives permitted by section 65915. (b) Grounds for Denial. In accordance with Government Code section 65915(e), the City may deny an applicant's request to waive or modify the City's development standards in any of the following circumstances: (1) The application does not conform with the requirements of this section or Government Code section 65915. (2) The applicant fails to demonstrate that the City's development standards physically preclude the utilization of a density bonus on a specific site. (3) The waiver or reduction would have a specific, adverse impact, as defined in Government Code section 65589.5(d)(2), upon health, safety, or the physical environment, and there is no feasible method to satisfactorily mitigate or avoid the specific adverse impact. (4) The waiver or reduction would have an adverse impact on any real property that is listed in the California Register of Historical Resources."
    },
    {
      "heading": "27.15.060 Application Procedure.",
      "id": "/us/ca/cities/san-mateo/code/27.15.060",
      "text": "(a) An applicant requesting a density bonus, incentive or concession, or waiver or modification of development standards, in accordance with this section must submit a written request with any application for a planning approval at the time the planning application is filed. The written request must include the following information: (1) The number of proposed affordable housing units; (2) Whether or not the applicant is proposing the use of state density bonus law parking standards; (3) the specific incentive(s) or concession(s) sought, if any; (4) the specific waiver or modification to development standards sought, if any; (5) if seeking an incentive or concession, documentation required by the Director of Community Development or his or her designee regarding the identifiable and actual cost reduction to provide affordable housing costs or rents; (6) if seeking a waiver or modification of development standards, documentation required by the Director of Community Development or his or her designee regarding the necessity of the waiver or modification, including documentation demonstrating that the City's development standards physically preclude the utilization of a density bonus; (7) If requesting a density bonus based on land donation in accordance with Government Code section 65915(g), the applicant must submit information sufficient to permit the City to determine that the proposed donation conforms with the requirements of section 65915(g) and this Code; (8) If requesting a density bonus based on the provision of a child care facility, the applicant must: (A) Provide the location of the proposed child care facility and the proposed operator; (B) Agree to operate the child care facility for a period of time that is as long as or longer than the period of time during which the density bonus units are required to remain affordable; (C) Agree to have contracted with a child care facility operator for operation of the child care facility before the first building permit is issued; and (D) Agree that the child care facility will be in operation when the first certificate of occupancy is issued. (b) Action on Application. The density bonus request will be processed with the planning application and the body with approval authority for the planning approval sought will approve, deny or modify the incentive or concession as a part of the overall project approval."
    },
    {
      "heading": "27.15.070 Affordable Housing Agreement.",
      "id": "/us/ca/cities/san-mateo/code/27.15.070",
      "text": "Prior to the issuance of a building permit for any dwelling unit in a development for which a density bonus has been awarded, the developer must enter into an Affordable Housing Agreement. The Agreement will run with the land, be binding upon successors in interest, and be recorded with the County Recorder.."
    },
    {
      "heading": "27.15.080 AFFORDABLE HOUSING PROJECTS NEAR TRANSIT",
      "id": "/us/ca/cities/san-mateo/code/27.15.080",
      "text": "(a) Applicability. This Section applies to housing developments in which 100 percent of the total units, exclusive of a manager's unit or units, are for lower income households (as defined in Section 50079.5 of the Health and Safety Code), except that up to 20 percent of the total units in the development may be for moderate-income households (as defined in Section 50053 of the Health and Safety Code) and located within a half-mile of a major transit stop as defined in Public Resources Code Section 21155 (\"Covered Projects\"). (b) Reduced Requirements for Covered Projects. When a development standard would physically preclude a proposed project from achieving allowable density, planning applications submitted for Covered projects may request waivers or reductions from up to six applicable development standards in addition to the incentives or concessions otherwise provided by state law. The request to waive or reduce development standards shall be considered by the decision-making body with the authority to act on the Covered Project, and shall be subject to the following findings: (1) The requested deviations will not conflict with the General Plan; (2) The development is of an excellent design quality and is consistent with applicable Design Guidelines; (3) The development is in the best interests of the public health, safety, or welfare; (4) The development will not impair the desirability of investment or occupation in the vicinity; and (5) The project has demonstrated use of all allowable incentives consistent with Government Code Section 65915."
    }
  ],
  "Chapter 27.16 RESIDENCE DISTRICTS": [
    {
      "heading": "27.16.010 USE AND BULK REGULATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.16.010",
      "text": "Use and bulk regulations applying specifically to residence districts are set forth in Chapters 27.18 through 27.26. Also applying to residence districts are additional regulations set forth in other chapters of this title as follows: (1) Chapters 27.01, 27.16, 27.66, 27.68, 27.70 and 27.82, General Provisions; (2) Chapter 27.04, Definitions; (3) Chapter 27.72, Nonconforming Buildings and Uses; (4) Chapter 27.64, Off-Street Parking and Loading; (5) Chapter 27.06 through 27.12, 27.62, 27.74, 27.78 and 27.80, Administration."
    },
    {
      "heading": "27.16.020 ACCESS TO PUBLIC STREET.",
      "id": "/us/ca/cities/san-mateo/code/27.16.020",
      "text": "Except as otherwise provided for in this title, every building in a residential district shall be constructed upon a lot which abuts upon a public street as shown on a subdivision map accepted by the City and as recorded in the office of the recorder of San Mateo County, or as designated by a resolution pursuant to Section 17.04.010, unless a permanent easement of access to a public street was of record prior to the effective date of this title, or unless approved pursuant to proceedings authorized by this title."
    },
    {
      "heading": "27.16.030 VEHICLE AND BOAT REPAIR.",
      "id": "/us/ca/cities/san-mateo/code/27.16.030",
      "text": "It is unlawful and a public nuisance for any person to engage in, or any property owner to allow to occur, vehicle or boat repair in any residential zone: (a) Upon any vehicle which is not registered to a current occupant of the premises where the work is being performed; or (b) Upon more than two (2) vehicles at one time on the same premises or by the same person; or (c) Outside a fully enclosed structure for uses defined as major motor vehicle repair as defined in Section 27.04. Minor motor vehicle repair may be performed outside a fully enclosed structure where elapsed time between the beginning and end of the repair does not exceed forty-eight (48) hours. Vehicle painting, other than spot painting, shall not be permitted in residential zones."
    },
    {
      "heading": "27.16.040 HOME OCCUPATION.",
      "id": "/us/ca/cities/san-mateo/code/27.16.040",
      "text": "Home occupations are permitted in dwellings upon approval of a Home Occupation Certificate by the City. All home occupations shall meet the following standards: (a) Allowable Uses. The home occupation shall be accessory to the primary use of the dwelling as a residence. Allowable uses include offices, professional services, instruction, food preparation, handicrafts, and other similar uses as authorized by the Zoning Administrator. Auto repair and retail sales from the dwelling are prohibited. Businesses selling or renting firearms, as defined by Penal Code section 12001(b), shall be prohibited unless a special use permit is approved, subject to compliance with the limitations set forth in this section and such other conditions as are established by the special use permit process. (b) Employees. Permanent residents of the dwelling are the only persons permitted to engage in or be employed in the home occupation at the residence. Workers shall not be allowed to physically report to the property for activities such as dispatching or assignment to off-site locations. (c) Allowable Area. The home occupation shall be limited to either four-hundred (400) square feet or twenty (20) percent of the floor area of the dwelling (excluding parking but including storage areas), whichever is less. An accurate floor plan shall be submitted as part of the Home Occupation Certificate, showing the area to be devoted to the home occupation, including any vehicles parking area. The use shall be conducted only in the primary residence of the employee or in an accessory structure on the same parcel. No area devoted to off-street parking required by Chapter 27.64 for the dwelling shall be used in any manner for the purpose of conducting a home occupation. (d) Client Visitation. Client visitation shall be limited to the hours between 8 a.m. and 6 p.m. A maximum of five (5) client visitations per day to the site is permitted. (e) Deliveries. Goods, materials, equipment or services delivered to or from the home occupation shall only be permitted by the home occupation employees, or by a private or government-operated mail service. Deliveries shall take place only between 8 a.m. to 6 p.m. and shall not take place more than twice daily. (f) Parking. Home occupations shall provide off-street parking for all vehicles owned by or registered to the business. However, one vehicle owned by or registered to the home occupation may utilize one of the dwelling unit's parking spaces if the vehicle is also the home occupation employee's primary personal transportation. Vehicles used in conjunction with the home occupation shall conform to the provisions of Chapter 11.32 of the City of San Mateo Municipal Code. (g) Outdoor display and storage. Outdoor display or storage of goods, equipment or material is prohibited. (h) Dwelling appearance. The home occupation shall not be conducted in a manner that changes the exterior character and appearance of the dwelling unit in which it is conducted. (i) Nuisance. The home occupation shall not be conducted in a manner which constitutes a public nuisance, or is offensive or hazardous. The home occupation shall not generate light, noise or vibration disruptive to the character of a residential neighborhood, or generate electrical or electronic interference. In no event shall the home occupation generate noise in excess of 45 dBA (LDN) when measured at any property line. The home occupation shall not generate garbage, refuse or recyclable material exceeding the amount normally associated with a residential use of the property. The use shall not utilize hazardous materials, and shall not create adverse effects, including, but not limited to, traffic, parking, crime, security matters, smoke or odors. (j) Business Tax. All required business taxes shall be timely paid."
    },
    {
      "heading": "27.16.050 AFFORDABLE HOUSING.",
      "id": "/us/ca/cities/san-mateo/code/27.16.050",
      "text": "To implement the affordable housing goals and policies in the General Plan, the City Council adopted the Below Market Rate (BMR) Program. Specific requirements for the development of affordable units are regulated by resolution adopted by the City Council."
    },
    {
      "heading": "27.16.070 BED AND BREAKFAST INN.",
      "id": "/us/ca/cities/san-mateo/code/27.16.070",
      "text": "Bed and breakfast inns are permitted in dwellings within all multiple family residential districts. It is unlawful to operate a bed and breakfast which does not meet all of the following requirements: (a) The use shall conform to the density standards of the zoning district in which the property is located. For the purpose of density, two guest rooms are the equivalent of one dwelling unit. However, in no case shall the total number of guest rooms exceed ten (10); (b) Maximum length of stay is fourteen (14) consecutive days; (c) The owner and manager of the business shall reside on the property; (d) No cooking facilities shall be allowed in guest rooms; and (e) Meals shall be provided only to guests and the on-site manager and family."
    }
  ],
  "Chapter 27.17 MANUFACTURED HOMES": [
    {
      "heading": "27.17.010 MANUFACTURED HOMES.",
      "id": "/us/ca/cities/san-mateo/code/27.17.010",
      "text": "Manufactured homes shall conform to the minimum lot size, yard areas, access, vehicular parking, and setbacks for the zone in which they are to be installed in addition to meeting the standards set forth in this ordinance."
    },
    {
      "heading": "27.17.020 DEFINITIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.17.020",
      "text": "(1) For purposes of permitting manufactured homes in residential zones, the following definitions shall apply: (a) \"Architectural features\" shall mean an architectural feature that occurs or appears frequently on conventionally-built homes within three hundred (300) feet from the boundaries of a parcel on which a manufactured home is proposed. (b) \"Manufactured home\" shall mean a structure, transportable in one or more sections, which, in the traveling mode, is eight body feet or more in width, or forty (40) feet or more in length, or when erected on site, is 320 or more square feet, and which is built on a permanent chassis and designed to be used as a dwelling with or without a permanent foundation when connected to the required utilities, and the plumbing, heating, air conditioning, and electrical systems are contained within the structure. \"Manufactured home\" shall also include any structure which meets all the requirements of this subsection except the size requirements and to which the manufacturer voluntarily has filed a certification and complies with the standards established by the Health and Safety Code. \"Manufactured home\" shall also include a mobilehome subject to the National Manufactured Housing Construction and Safety Act of 1974. \"Manufactured home\" shall include only those structures that contain two or less dwelling units, and that conform to the applicable requirements of the laws of the State of California or United States. (c) \"Manufactured home\" shall mean a dwelling manufactured off-site, conforming to state or federal standards, (bearing a state, or federal label) and transportable in one or more sections, designed to be installed on a permanent foundation. (d) \"Permanent foundation\" shall mean assembly of materials constructed below, or partially below grade, not intended to be removed from its installation site, which is designed to support a manufactured home structure and engineered to resist the imposition of external natural forces, as defined by the Health and Safety Code or the Building Code, whichever is more restrictive."
    },
    {
      "heading": "27.17.030 MANUFACTURED HOME TAXATION.",
      "id": "/us/ca/cities/san-mateo/code/27.17.030",
      "text": "The initial installation of a manufactured home on a parcel which has been installed on a permanent foundation pursuant to this ordinance shall be deemed to be a manufactured home subject to local property taxation pursuant to the Health and Safety Code and the Revenue and Taxation Code. Upon issuance of a certificate of occupancy, the City shall record with the County Recorder the specifics of such permanent installation and, also, advise the State Department of Housing and Community Development."
    },
    {
      "heading": "27.17.040 SPAR.",
      "id": "/us/ca/cities/san-mateo/code/27.17.040",
      "text": "A manufactured home unit on a permanent foundation on a private lot may be permitted subject to the approval of a site plan and architectural review (SPAR) application by the Zoning Administrator. The applicant/owner shall also provide the information required on the MH Form. Subsequent modifications, such as, room additions, shall be subject to issuance of a building permit."
    },
    {
      "heading": "27.17.050 ELIGIBILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.17.050",
      "text": "A manufactured home shall not be installed on a permanent foundation on a private parcel unless it: (a) Was constructed after September 15, 1971, and was issued an insignia of approval by the California Department of Housing and Community Development or was constructed after July 1, 1976, and was issued a label of approval by the United States Department of Housing and Urban Development; and (b) Has not been altered in violation of applicable federal and state codes; and (c) The board, upon the findings and recommendations of its members shall determine the eligibility of each mobilehome unit to be installed."
    },
    {
      "heading": "27.17.060 STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.17.060",
      "text": "A manufactured home located on a permanent foundation on a private parcel shall: (a) Be occupied only as a residential use type. (b) Be subject to all provisions of the Municipal Code applicable to conventional residential structures. (c) Meet all development and design standards for the zone in which they are to be installed, including but not limited to the parking standards in Chapter 27.64 conforming to the maximum floor area ratio, and including landscape requirements, as applicable. (d) Be attached to a permanent foundation in compliance with all applicable building regulations, and of the health and Safety code. (e) Have a minimum width of twenty (20) feet or be a double-wide, multi-sectional unit. (f) Be covered with exterior building materials and have architectural features customarily used on conventional residential dwellings and be approved by the board. The exterior covering material shall extend to finished grade, except that when a solid concrete or masonry perimeter foundation is used, the exterior covering material need not extend below the top of the foundation. (g) Have a roof with a pitch of not less than two (2) inch vertical rise for each twelve (12) inch of horizontal run and consisting of shingles or other material customarily used for conventional residential dwellings. (h) Assure that the general appearance of the structure and property is in keeping with the character of the neighborhood. To achieve this assurance, the board shall require porches and eaves or roofs with eaves, specific roofing materials and siding when, in its opinion, it is necessary to be compatible with the dwellings in the area. The board shall assure that: (1) All windows and doors be architecturally treated in a manner complimentary to the building's overall design and shall comply to the City's security standards. (2) Screening be provided for all mechanical and electrical equipment, so that they are not visible from the public right-of-way. For roof and wall mounted equipment, the screening shall be an integral part of the building design. (3) Exterior materials shall generally consist of those permitted by the Building Code. Shiny, metallic surfaces are unacceptable. (i) Be provided with standard utility connections. The housing unit electrical, gas, water and drain connections shall be made permanent in a manner applicable to permanent buildings. Gas shutoff valves, meters and regulators shall not be located beneath the manufactured home. (j) Obtain a site development permit pursuant to Chapter 23.40 of this code."
    },
    {
      "heading": "27.17.070 MODIFICATION OF STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.17.070",
      "text": "Modification of the standards set forth in section 27.17.060, paragraphs (e), (f) and (g), may be granted by the board if it finds that such modification will not be detrimental to the public interest or surrounding residents or properties."
    },
    {
      "heading": "27.17.080 SURRENDER OF REGISTRATION.",
      "id": "/us/ca/cities/san-mateo/code/27.17.080",
      "text": "Subsequent to applying for the required building permits, and prior to occupancy, the owner shall surrender the certificate of title or other indicia of registration to the state department of community development pursuant to section 18551(b) of the California Health and Safety Code. Thereafter, any vehicle license plate, certificate of ownership, and certificate of registration issued by a state agency is to be surrendered to the appropriate state agencies. Any manufactured home which is permanently attached to a permanent foundation must bear a California insignia or federal label, pursuant to section 18550(b) of the Health and Safety Code."
    },
    {
      "heading": "27.17.090 BUILDING PERMIT.",
      "id": "/us/ca/cities/san-mateo/code/27.17.090",
      "text": "Prior to installation of a mobilehome on a permanent foundation, the mobilehome owner or a licensed contractor shall obtain a building permit from the City building division. To obtain such a permit, the owner or contractor shall comply with all requirements of section 18551(a) of the State Health and Safety Code."
    }
  ],
  "Chapter 27.18 R1 DISTRICTS—ONE FAMILY DWELLINGS": [
    {
      "heading": "27.18.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.18.010",
      "text": "The R1 Single-Family Residence Districts are intended to create, preserve and enhance areas suitable for single-family dwellings with a substantial presence of open space and opportunities for outdoor living. The R1 districts are intended to protect the character and variety of neighborhoods, preserve privacy and prevent burdens on public facilities, while allowing reasonable housing opportunities for families."
    },
    {
      "heading": "27.18.020 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.18.020",
      "text": "The following uses are permitted: (a) One-family detached dwellings, including manufactured homes on permanent foundations subject to provisions of Chapter 27.17; (b) Accessory dwelling units and junior accessory dwelling units subject to the provisions of Chapter 27.19; (c) Accessory uses and structures; (d) Detached accessory structures containing no more than two (2) plumbing fixtures or waste lines; (e) Home occupations, subject to provisions of Section 27.16.040; (f) Community care facilities licensed by the State of California for the following: (1) Six (6) or fewer occupants, in addition to the caregiver's family, and (2) Family day care for fourteen (14) or fewer occupants, in addition to the caregiver's family, when managed in the caregiver's residence and in accordance with State law; and (g) Temporary buildings for construction purposes for a period not to exceed the duration of such construction."
    },
    {
      "heading": "27.18.030 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.18.030",
      "text": "The following uses may also be allowed if a special use permit is approved: (a) Detached accessory structures, other than secondary units, containing more than two (2) plumbing fixtures or waste lines; (b) Swimming pools, hot tubs and spas located in required front yard or street side yard; (c) Cemeteries, mausoleums, and columbaria, subject to the provisions of the Section 27.18.120; (d) Churches, convents, parish houses, and monasteries, including as a permitted accessory use emergency shelters subject to the requirements in a residential zone; (e) Community services including but not limited to libraries, parks, playgrounds, and community centers; (f) Public and private educational facilities; (g) Day care centers when located within a public or quasi-public structure such as a school, recreation center, church, temple or similar facility; (h) Philanthropic and eleemosynary uses; (i) Public utility facilities; and (j) Temporary real estate sales offices for a period not to exceed the duration of the construction and sale of homes within the subdivision wherein the sales office is to be located."
    },
    {
      "heading": "27.18.035 SUBSTANTIAL REMOVAL OF EXISTING RESIDENCE.",
      "id": "/us/ca/cities/san-mateo/code/27.18.035",
      "text": "(a) A special use permit shall be required for the substantial removal of an existing residence, regardless of whether it is currently inhabited. \"Substantial removal\" shall mean the demolition of 50% or more of the structure's exterior walls (measured in lineal feet) and/or roof (measured in square feet). Existing exterior walls that are converted to interior walls shall be counted as walls to be demolished. Substantial removal for a roof shall not apply to permit applications for re-roofing where roof pitch alterations do not exceed an increase in height of more than two (2) feet as measured at the highest point or where a Single Family Dwelling Design Review (SFDDR) planning application has been submitted as part of the proposed dwelling's improvements. Doors, including garage doors, entry doors, and sliding glass doors, shall not be included in the percentage calculation of an existing structure's exterior walls. This section shall not apply to an accessory building or to a residence that has been declared a public nuisance under this Code. (b) No existing residence may be substantially removed unless either: (1) an application for a residence is submitted concurrently with the application for removal and is approved pursuant to the SFDDR procedures; or (2) plans for a permitted use other than a residence are submitted concurrently with the application for removal and, if the permitted use does not contain a principal structure, removal shall be conditioned upon subsequent SFDDR of a new principal structure; or (3) application for a special use permit is submitted concurrently with the application for removal and is approved; if the special use permit does not contain a principal structure, removal shall be conditioned upon subsequent SFDDR of a new principal structure."
    },
    {
      "heading": "27.18.040 PARCEL SIZE STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.18.040",
      "text": "(a) Newly created parcels. Dwellings developed after the effective date of this title shall be developed on recorded parcels which meet the following prescribed standards: (b) Existing substandard parcels. Dwellings may be erected on parcels which do not meet the minimum standards of section (a) above if the parcel was recorded under separate ownership from adjoining parcels prior to March 3, 1947, if the subdivision map was approved with exceptions or if a recorded parcel has received a certificate of compliance. (c) Width at street frontage. All parcels shall provide a minimum width of thirty (30) feet on a recorded public street frontage, or on a street as designated by resolution pursuant to Section 17.04.010. However, less width may be provided, if a permanent access easement to a public street was either recorded prior to this title's effective date, or is approved by the City."
    },
    {
      "heading": "27.18.050 BUILDING HEIGHT AND DAYLIGHT PLANE.",
      "id": "/us/ca/cities/san-mateo/code/27.18.050",
      "text": "(a) Maximum height. The maximum height of structures shall be 24 feet measured from existing grade to the building plate line and 32 feet measured from the existing grade to the highest point of the roof. Existing residences that exceed these limits may construct additions in accordance with their existing roof lines but shall not increase the non-conformance with these height limits. (b) Daylight plane. No structure shall extend above or beyond a daylight plane having a height of twelve (12) feet at each side property line and extending into the parcel at an angle of forty-five (45) degrees, with the following encroachments allowed:  (1) Television and radio antennas, chimneys, flues, eaves, or skylights; (2) Dormers or similar architectural features, provided that the horizontal length of all such features shall not exceed a combined total of fifteen (15) feet on each side, measured along the intersection with the daylight plane;  (3) Gables or similar architectural features, provided that the horizontal length of all such features shall not exceed a combined total of eighteen (18) feet on each side, measured along the intersection with the daylight plane, and provided that the intersection of the gable with the daylight plane closest to the front property line is along the roof line;  (4) Where the finished first floor of an existing dwelling is more than three (3) feet above existing grade and is being extended by an addition, the initial height of the daylight plane shall be fourteen (14) feet; (5) Where the slope of a parcel measured between the side property lines at the front setback is fifteen percent (15%) or steeper, the initial height of the daylight plane shall be fourteen (14) feet on the downhill side of the parcel; and  (6) Where the slope of a parcel measured between the front and rear most points of the structure is fifteen percent (15%) or steeper, the daylight plane shall be measured at the front setback line and each thirty (30) feet thereafter, and the height limits established at these points shall be extended horizontally to the next measurement point. "
    },
    {
      "heading": "27.18.060 FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.18.060",
      "text": "The floor area ratio of buildings and structures on a parcel shall not exceed the following limitations: In no case shall more than 6,000 square feet of total floor area be permitted per parcel in residential use."
    },
    {
      "heading": "27.18.070 Front Yard",
      "id": "/us/ca/cities/san-mateo/code/27.18.070",
      "text": "(a) A front yard setback not less than twenty-five (25) feet in an R1-A district and not less than fifteen (15) feet in an R1-B or R1-C district shall be provided. (b) Garage setback. A front yard setback not less than twenty (20) feet in an R1-B or R1-C district shall be provided for a garage. (c) Private roads. Buildings erected or enlarged on property fronting upon a private road or easement shall maintain a front setback of at least fifty (50) feet from the centerline of such private road or easement. (d) Limits on paving. This subsection regulates the amount and location of paving in order to: (1) maintain an aesthetic, landscaped appearance along the street frontages; and (2) maximize the amount of usable open space and landscape areas for single-family properties. The portion of the required front yard setback that is paved shall be limited to driveways or walkways. The paving (including pervious and non-pervious surfaces), shall be limited to: (1) that required for necessary driveway, as follows: (A) Single car garages: 17 feet maximum in width or 40% of the street frontage, whichever is less, beginning at the side property line adjacent to the driveway, and including any contiguous paving (i.e. pedestrian walkways) with the following exception: (i) For those parcels with single car garages, carports, or open parking spaces setback more than 35 feet from the front property line, no paving in addition to the driveway shall be allowed in the front yard setback. (B) Two-car garages or larger: 20 feet maximum in width. (C) For properties located on a cul-de-sac, a driveway at least 10 feet in width shall be permitted when providing access to two or fewer garages, carports, or open parking spaces, and 12 feet in width when providing access to three or more garage, carport, or open parking spaces; (2) Circular driveways subject to SPAR review; and (3) Pedestrian walkways which are five (5) feet or less in width. (e) Landscaping. Other than the paving for driveway and walkway that are permitted in subsection (d) above, the remaining portion of the required front yard setback is intended to: (1) be improved with landscaping and elements for outdoor living, and (2) provide space for the preservation of heritage trees. Parking is prohibited in outdoor living areas and in areas delineated in Section 27.64.023 of the San Mateo Municipal Code."
    },
    {
      "heading": "27.18.080 Side Yards",
      "id": "/us/ca/cities/san-mateo/code/27.18.080",
      "text": "(a) Interior side yards. Interior side yard setback not less than seven (7) feet in an R1-A district and not less than five (5) feet in an R1-B or R1-C district shall be provided. (b) Street side yards. For corner parcels, a side yard adjacent to the street is a street side yard and a setback is required as follows: (1) For ground floors: Fifteen percent (15%) of the lot width as measured at building location, not less than 7.5 feet and not to exceed 25 feet in the R1-A district and 15 feet in the R1-B and C districts. (2) For construction above the first story: Minimum of ten (10) feet. (3) For garages: Minimum of twenty (20) feet. (4) Limits on paving. This subsection regulates the amount and location of paving in order to: (1) maintain an aesthetic, landscaped appearance along the street frontages; and (2) maximize the amount of usable open space and landscape areas for single-family properties. The portion of the required street side yard setback that is paved shall be limited to driveways or walkways. The paving (including pervious and non-pervious surfaces), shall be limited to: (A) that required for necessary driveways, as follows: (i) Single car garages: 17 feet maximum in width or 40% of the street frontage whichever is less, beginning at the side property line adjacent to the driveway, and including any contiguous paving (i.e. pedestrian walkways) with the following exception: (I) For those parcels with single car garages, carports, or open parking spaces setback 35 feet or more from the street property line, no paving in addition to the driveway shall be allowed in the side setback. (ii) Two-car garages or larger: 20 feet maximum in width. (B) Pedestrian walkways which are five (5) feet or less in width. (5) Landscaping. Other than the paving for driveway and walkway that are permitted in subsection (4) above, the remaining portion of the required street side yard setback is intended to: (1) be improved with landscaping and elements for outdoor living, and (2) provide space for the preservation of heritage trees. Parking is prohibited in outdoor living areas and in areas delineated in Section 27.64.023 of the San Mateo Municipal Code. (c) Extensions of walls having non-conforming side yards. When an existing interior side yard of a legally constructed single-family dwelling is less than that required by this Section, a single story, horizontal addition may be constructed maintaining the existing non-conforming setback line, provided that: (1) The existing side yard setback to be extended is at least three (3) feet from the side property line; (2) The maximum height of the extended wall is twelve (12) feet to the plateline; (3) The total length of the extension along a single side wall shall not exceed twenty (20) feet; and (4) The proposed extension is the subject of Site Plan and Architectural Review (SPAR) conducted by the Zoning Administrator pursuant to the provisions of Section 27.08.030. (d) Non-residential uses. Newly constructed or expanded structures for non-residential uses allowed under Section 27.18.030 shall provide minimum side yards, both interior and street, of fifteen (15) feet or one-half the building height, whichever is greater."
    },
    {
      "heading": "27.18.090 REAR YARD.",
      "id": "/us/ca/cities/san-mateo/code/27.18.090",
      "text": "A rear yard of not less than fifteen (15) feet shall be provided; a rear yard not less than twenty-five (25) feet shall be provided for new construction above a single story.  "
    },
    {
      "heading": "27.18.100 STRUCTURES AND BUILDING PROJECTIONS IN REQUIRED YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.18.100",
      "text": " (a) The following structures, building projections and features shall be permitted in all yards: (1) Arbors and trellises, having a maximum height of eight (8) feet, except in no case shall any such structure be used to cover driveways located in required setbacks in the front 2/3 of the property; (2) Awnings, canopies and covered patios, having a maximum height of eight (8) feet; (3) Basements completely below grade; (4) Eaves, projecting a maximum of three (3) feet of fifty percent (50%) of the required yard width, whichever is less; (5) Chimneys, solariums, greenhouse windows and oriel bay windows projecting two (2) feet or less into the yard, provided that the outside face of the projections shall be at least three (3) feet from the property line; (6) Balconies and decks projecting two (2) feet or less into the yard, excluding projections into interior side yards above the first floor, and provided that the outside face of the projection shall be at least three (3) feet from the property line; (7) Flag poles, garden ornaments and play equipment; (8) Steps which are necessary to provide access to the first floor of a permitted building, or to a parcel from a street or alley; (9) Uncovered decks, subject to the following standards: (A) Uncovered decks that are eighteen (18) inches in height, or shorter, are allowed in all required yards; and (B) Uncovered decks that are taller than eighteen (18) inches and no taller than thirty (30) inches in height are allowed in some portions of required yards provided that they are not located within five (5) feet of property lines. (10) Open parking spaces within a rear yard. (b) The following structures, building projections and features shall be permitted in front yards: Covered porches projecting two (2) feet or less into required front yards, and only when the required yard meets current yard setback requirements. The projection into the required yard may not be enclosed with walls or other material. The projection shall not exceed 50% of the width of the house as measured at the front property line, (c) Location of detached accessory buildings. A detached accessory building located within the rear one-third of a parcel is exempt from the requirements for interior side and rear yards, provided that such structure: (1) Shall be separated from the principal building by a distance not less than four (4) feet in width that is open to the sky, and (2) Shall not exceed a height of nine (9) feet to the plate line and sixteen (16) feet to the roof peak, and (3) Shall not extend above or beyond a daylight plane having a height of nine (9) feet at each side and rear property line and extending into the parcel at an angle of forty-five (45) degrees, excepting eaves and flues, and (4) Shall be limited to one habitable floor on the ground level. Habitable floor for the purposes of this subsection shall mean that served by permanent access and containing windows and/or plumbing fixtures, but shall exclude basements. (d) Maximum coverage of required rear yards. Accessory buildings shall not occupy more than fifty (50) percent of a required rear yard. "
    },
    {
      "heading": "27.18.110 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.18.110",
      "text": "(a) Off-street parking facilities shall be required for all permitted and special uses in accord with Chapter 27.64. (b) Minimum parking requirements for single family uses permitted in the R1 Districts shall be as follows: (c) Location in required yards. Required parking may not be located within a required front yard or side yard. (d) Garage doors. For garages located within fifty (50) feet of a street frontage, no more than fifty (50) percent of the ground floor building facade facing the street shall be composed of garage doors or open covered parking facilities."
    },
    {
      "heading": "27.18.115 San Mateo Park Planning Area",
      "id": "/us/ca/cities/san-mateo/code/27.18.115",
      "text": "Notwithstanding other provisions of this chapter, the following shall be applicable to the San Mateo Park planning area as is designated on the map shown below:  (a) For both new residences and additions to existing residences: (1) Garages shall provide a front yard setback of at least 50 feet when garage doors face the street, or 25 feet if garage doors do not face the street, except in cases where an existing or previously existing garage faced the street with less than a 50 foot front setback and in those cases the new garage may face the street with a front yard setback equal to or greater than that which previously existed and with no increase in the number of garage spaces that face the street. (2) Sideyard setbacks shall be a minimum of 10 feet for interior lots of widths equal to or greater than 75 feet and 7 feet for interior lots of widths less than 75 feet. (b) For additions to existing residences: (1) Street sideyard setbacks shall be equal to 15% of the lot width as measured at the building location but not less than 10 feet nor more than 25 feet. (c) For new residences constructed on corner lots of widths equal to or greater than 75 feet: (1) Both street frontages shall be treated as front yards with a minimum setback of 25 feet."
    },
    {
      "heading": "27.18.120 CEMETERIES, MAUSOLEUMS, AND COLUMBARIA.",
      "id": "/us/ca/cities/san-mateo/code/27.18.120",
      "text": "Cemeteries, mausoleums, and columbaria shall be subject to the following use conditions: (a) Cemeteries, mausoleums, and columbaria shall be closed from sunset to 7:00 a.m., and all gates shall be locked during the hours of closure. Signs indicating hours shall be prominently displayed at all entry/exit gates at all times. (b) The minimum setback for cemeteries existing on November 16, 1992, shall be established by resolution of the City Council or shall be as shown on a previously issued special use permit. Minimum setbacks for new cemeteries shall not be less than the setbacks established for R1-A districts and shall be established as part of the special use permit process. No burials may be located within setbacks excepting those burials that have occurred on or before November 16, 1992. (c) A special use permit shall be required for construction or placement of mausoleums, columbaria, monuments, or other above ground structures that exceed a height of four (4) feet above grade. However, no mausoleum, columbarium, or monument exceeding a height of seven (7) feet above grade shall be permitted. (d) Applicants for a special use permit for a cemetery use shall be required to submit a landscape plan for setback areas as part of the application. (e) Cemeteries shall be required to upgrade parking facilities in compliance with the standards of Chapter 27.64 as part of the special use permit process."
    }
  ],
  "Chapter 27.19 ACCESSORY DWELLING UNIT AND JUNIOR ACCESSORY DWELLING UNIT—RESIDENTIAL ZONES": [
    {
      "heading": "27.19.010 Purpose.",
      "id": "/us/ca/cities/san-mateo/code/27.19.010",
      "text": "The purpose of this Article is to set forth regulations to permit accessory dwelling units (ADUs) in accordance with state law."
    },
    {
      "heading": "27.19.020 Reserved.",
      "id": "/us/ca/cities/san-mateo/code/27.19.020",
      "text": ""
    },
    {
      "heading": "27.19.030 Prohibition on Sale and Limitation on Rental.",
      "id": "/us/ca/cities/san-mateo/code/27.19.030",
      "text": "(a) An ADU shall not be sold separately from the primary residence. (b) If an ADU is rented, the unit shall not be rented for a period of less than 30 consecutive calendar days."
    },
    {
      "heading": "27.19.040 Ministerial Permit Approval.",
      "id": "/us/ca/cities/san-mateo/code/27.19.040",
      "text": "An ADU permit application for either an attached or a detached ADU is required in order to demonstrate that a unit is in compliance with the provisions of this Article. If the ADU is in full compliance with the provisions of this Article, a ministerial, non-discretionary permit will be issued. Notwithstanding anything to the contrary in this Code, the issuance of a ministerial ADU permit is not appealable."
    },
    {
      "heading": "27.19.045 Discretionary Review as Alternative to Ministerial Approval.",
      "id": "/us/ca/cities/san-mateo/code/27.19.045",
      "text": "(a) As an alternative to ministerial review, an applicant may submit an application for discretionary review of an ADU proposal that is not in full compliance with the provisions of this Article. (b) The application for discretionary approval shall be granted if the Zoning Administrator finds each of the following: (1) The proposed ADU is consistent with all applicable objective design standards in the adopted R1 Single-Family Dwelling Design Guidelines; (2) The proposed ADU would not result in a negative privacy impact on an abutting residential lot; and (3) The proposed ADU would not result in a negative impact to public health, safety, or welfare. (4) The proposed ADU, when detached and exceeding the height limit, should provide at least one additional off-street parking space. (c) The decision of the Zoning Administrator shall not preclude the ability of an applicant to receive a ministerial permit pursuant to Section 27.19.040 for an ADU that is in full compliance with the provisions of this Article. (d) The decision of the Zoning Administrator may be appealed to the Planning Commission, and the decision of the Planning Commission may be appealed to the City Council, in accordance with SMMC 27.08.090."
    },
    {
      "heading": "27.19.050 Development Standards",
      "id": "/us/ca/cities/san-mateo/code/27.19.050",
      "text": "An ADU, as defined in Section 27.04.165, shall comply with the following development standards: (a) Permitted Zoning Districts. ADUs shall only be constructed on a lot zoned to allow residential uses. (b) Number of Units. No more than the number of ADUs allowed by state law may be constructed on any lot. (c) State Exempted \"By Right\" ADUs. An attached or detached ADU of at least 800 square-feet in size and of at least 16 feet in building height with four-foot side and rear setbacks may be constructed on a lot regardless of any size limitation based on the size of the proposed or existing primary dwelling, lot coverage, floor area ratio, daylight plane, open space, or minimum lot size that would otherwise preclude or limit its construction. The floor area of any new ADU in excess of 800 square feet shall be applied to the maximum floor area allowance of the subject lot as prescribed by the underlying zoning district. (d) Maximum Unit Size. Floor area size maximums for both attached and detached ADU development in excess of 800 square feet are governed by the floor area maximum established by the underlying zoning district and remaining floor area allowance available on the lot. In instances when the existing floor area allowance of a lot has been fully utilized, only the state exempted \"by right\" ADU of up to 800 square feet is permitted. (1) Accessory Dwelling Unit Conversions. An ADU conversion within the walls of an existing primary residence or accessory structure is not subject to size requirements. ADU conversions may be expanded up to 150 square feet beyond the existing footprint provided the expansion is used to accommodate ingress and egress to the ADU. (2) Detached Accessory Dwelling Unit and Junior Accessory Dwelling Unit. Subject to the floor area requirements, one new detached ADU may be constructed on a lot with a junior accessory dwelling unit (JADU). (e) Height. The specific height maximums are applicable to all zoning districts which permit ADUs. (1) Attached Accessory Dwelling Units. Maximum building height for an attached ADU is 24 feet to top plateline and 32 feet to roof peak as measured from existing grade. (2) Detached Accessory Dwelling Units. Maximum building height for a detached ADU is 16 feet to top plateline and 24 feet to roof peak as measured from existing grade. (3) Alternative Discretionary Review for Detached Accessory Dwelling Units. For a detached ADU proposed to exceed the height limit, an application for discretionary review, pursuant to Section 27.19.045, shall be submitted. (f) Setbacks. An ADU shall have setbacks as follows: (1) No setback shall be required for an existing legally permitted garage or accessory structure that is converted to an ADU which is constructed in the same location and to the same dimensions as the existing structure. (2) A minimum setback of four feet shall be required from the side and rear lot lines for all new ADU construction not meeting the criteria set forth in subsection (1) above, including ADUs constructed above an existing legally permitted garage. (3) A minimum setback from the front lot line, as required in the lot's underlying zone district, shall be required for all new ADU construction not meeting the criteria set forth in subsection (1) above, including ADUs constructed above an existing legally permitted garage. (g) The ADU, whether attached or detached, shall provide a separate exterior entrance, and permanent provisions for living, sleeping, eating, cooking, and sanitation. (h) Location of Accessory Dwelling Unit. The ADU may be within, attached to, or detached from the primary dwelling unit. ADUs shall be accessory to the primary residence and are permitted in the same locations on the parcel as the primary residence as specified in the underlying zoning district. (i) Number and Type of Required Parking Spaces. (1) General Requirements. There shall be a minimum of one standard size off-street parking space for each ADU. All required parking spaces shall be a minimum of 10 feet wide by 18 feet long without any obstructions. Parking associated with ADU or JADU development, whether required or voluntary, must be located entirely on the same lot, and may be provided in a garage, carport, uncovered, or in tandem orientation. Additionally, maximum driveway width for single-car garages may be up to 20 feet to accommodate additional off-street parking. The required parking for the primary residential dwelling unit must comply with current standards, as specified by the underlying zoning district. (2) Location of Parking for Accessory Dwelling Units. Parking for the accessory dwelling unit may be located in the required front, side, and rear yard setback areas. (3) Replacement off-street parking is not required when a garage, carport, or covered parking structure is demolished in conjunction with the construction of an ADU or converted to an ADU. (4) Parking Exemptions. No additional off-street parking shall be required for an ADU in the following instances: (A) The ADU is located within one-half (1/2) mile walking distance of public transit; or (B) The ADU is located within an architecturally and historically significant historic district; or (C) The ADU is in part of the proposed or existing legally permitted primary residence or an existing legally permitted accessory structure; or (D) In an area requiring on-street parking, permits are required but not offered to the occupant of the ADU; or (E) When the ADU is located within one block of a car share location. (5) Voluntary Parking. If no parking space is required, a maximum of one off-street parking space per ADU or JADU may be voluntarily provided. (j) Architectural Standards. New ADUs and conversions of an existing legally permitted structure shall be designed to comply with the following standards: (1) Attached Accessory Dwelling Units. ADUs that are attached to the primary dwelling unit shall: (A) Be of the same architectural style as the primary dwelling unit; (B) Be constructed of similar exterior materials, finishes, and family of colors as the primary dwelling unit; (C) Offset windows from neighbor's windows to maximize privacy; and (D) Be designed to meet the daylight plane requirements of the R-1 zoning district as applied to the nearest adjacent side and rear lot lines. (i) Application of the daylight plane requirement shall not preclude a State Exempted \"By Right\" ADU as defined in this Chapter. (2) Detached Accessory Dwelling Unit. An ADU that is detached from the primary dwelling unit shall: (A) In instances when an ADU is attached to an accessory structure, provide a uniform and integrated design with that accessory structure; (B) Offset windows from neighbor's windows to maximize privacy; (C) Provide and maintain obscured glazing on second-story windows up to five feet from the finished floor when the windows are located within five feet of a lot line with an abutting residential lot; (D) When an exterior staircase is proposed, it shall have a setback of at least five feet from the nearest lot line and the size of the second story landing shall be limited to the minimum area required to allow ingress and egress as specified by the California Building Code; (i) For an ADU that seeks to have a larger second story deck, an application for discretionary review, pursuant to Section 27.19.045, shall be submitted. (E) Be designed to meet the daylight plane requirements of the R-1 zoning district as applied to the nearest adjacent side and rear lot lines. (k) Development Impact Fees. Development impact fees for ADUs shall be established in an amount set forth by resolution of the City Council. (l) Utility Service. If an ADU is constructed within existing space, a separate water connection, a sewer service connection, or power connection is not required for an ADU. If an ADU is not constructed within existing space, the City may require new or separate utility connections. (m) Utility Fees. For an ADU located within an existing structure, payment of a connection fee or capacity charge is not required. For an ADU that is separate from an existing structure, the City will require payment of a connection fee or capacity charge that is proportionate to the ADU's burden. (n) Address Assignment. An application for a building permit for an ADU must include application for a separate address assignment. (o) Other Requirements. All other zoning requirements shall be complied with unless an authorized variance is approved. (p) For ADUs proposed within an existing multi-family structure or on a lot with an existing multi-family dwelling, the provisions of Government Code Section 65852.2(e)(1) apply."
    },
    {
      "heading": "27.19.060 Reserved.",
      "id": "/us/ca/cities/san-mateo/code/27.19.060",
      "text": ""
    },
    {
      "heading": "27.19.070 Purpose.",
      "id": "/us/ca/cities/san-mateo/code/27.19.070",
      "text": "The purpose of this Article is to set forth regulations to permit junior accessory dwelling units (JADUs)."
    },
    {
      "heading": "27.19.080 Reserved.",
      "id": "/us/ca/cities/san-mateo/code/27.19.080",
      "text": ""
    },
    {
      "heading": "27.19.090 Prohibition on Sale and Limitation on Rental.",
      "id": "/us/ca/cities/san-mateo/code/27.19.090",
      "text": "(a) A JADU shall not be sold separately from the primary residence. (b) If a JADU is rented, the unit shall not be rented for a period of less than 30 consecutive calendar days."
    },
    {
      "heading": "27.19.100 Ministerial Permit Required.",
      "id": "/us/ca/cities/san-mateo/code/27.19.100",
      "text": "A JADU permit application is required in order to demonstrate that the unit is in compliance with the provisions of this Article. If the JADU is in full compliance with the provisions of this Article, a ministerial, non-discretionary permit shall be issued."
    },
    {
      "heading": "27.19.110 Development Standards.",
      "id": "/us/ca/cities/san-mateo/code/27.19.110",
      "text": "A \"junior accessory dwelling unit,\" as defined in Section 27.04.165, must comply with the following development standards: (a) Permitted Zoning Districts. JADUs shall only be constructed on lots zoned to allow single-family residential use, or for which a single-family residence exists or is proposed to be built. The residential lot shall not be part of a condominium, townhouse, or other multi-family development. (b) Limit to the Number of Junior Accessory Dwelling Units. The number of JADUs is limited to one per residential lot with a single-family residence. Lots with multi-family housing or more than one detached single-family dwelling are not eligible for JADUs. (c) Setback and Other Zoning Regulations. For purposes of setbacks and other zoning regulations, the JADU shall be considered to be a part of the principal use of subject site and shall be subject to the same requirements of the underlying zoning district. (d) Maximum Unit Size. The floor area of a JADU shall not exceed 650 square feet, including attic and basement areas as defined in Section 27.04.200 for the applicable zoning district. (e) Construct within Existing Structure. The JADU shall be constructed within the walls of the proposed or legally existing single-family dwelling unit, including an attached garage. Detached accessory structures, including detached garages or carports, are not permitted to be converted into JADUs. (f) Unit Access. A JADU must include: (1) A separate exterior entry from the main entrance to the single-family dwelling, which shall be provided to serve the JADU only; and (2) An interior entry access between the JADU and the single-family dwelling. This interior entry access may be a door equipped with a double lock. A permitted JADU may include a second interior door for sound attenuation. (g) Efficiency Food Preparation Area. A JADU shall include an efficiency kitchen that includes the following components: (1) Cooking facility with appliances; and (2) Food preparation counter and storage with cabinets that are of reasonable size in relation to the size of the JADU. (h) Sanitation Facilities. A JADU may include its own separate sanitation facilities or may share sanitation facilities with the primary dwelling unit. (i) Building and Fire Requirements. (1) No fire wall separation or noise attenuation measures are required between the main dwelling and the JADU. No fire sprinklers are required for the JADU, unless the associated improvements meet the threshold for a \"substantial remodel\" as defined by Chapter 23, Building and Construction, of the San Mateo Municipal Code. The JADU shall have an adjoining door connected to the main living area for fire separation. A smoke alarm shall be required in the JADU and shall be connected to the smoke alarm in the main residence. (2) The JADU shall be equipped with a carbon monoxide detector. (j) Utility Service. A separate water connection, a separate sewer service connection, and power connection as water, sewer, and power service is not required for a JADU. (k) Parking. No additional off-street parking is required for a JADU. (l) Address Assignment. An application for a building permit for a JADU must include application for a separate address assignment."
    },
    {
      "heading": "27.19.120 Recordation of Deed Restriction.",
      "id": "/us/ca/cities/san-mateo/code/27.19.120",
      "text": "(a) A deed restriction shall be recorded to run with the land and submitted to the City prior to building permit issuance which indicates the following: (1) The property owner must occupy either the single-family residence or the JADU. (2) If the JADU is rented, the unit shall not be rented for a period of less than 30 consecutive calendar days. (3) Sale of the JADU separately from the single-family residence is prohibited. (4) The approved size and attributes of the JADU. (b) A copy of this deed restriction must be given to each prospective occupant."
    }
  ],
  "Chapter 27.20 R2 DISTRICTS—TWO FAMILY DWELLINGS": [
    {
      "heading": "27.20.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.20.010",
      "text": "No building or land in the R2 district shall be used and no building shall be hereafter erected, structurally altered or enlarged, unless otherwise provided in this title, except for the following: (a) Any use permitted in the R1 districts, subject to the same regulations and exceptions; (b) Two family dwellings; (c) Accessory uses which are necessary to the above-mentioned buildings and uses."
    },
    {
      "heading": "27.20.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.20.020",
      "text": "Special uses in the R2 districts shall be any special uses permitted in the R1 district, the subject to the same regulations and exceptions."
    },
    {
      "heading": "27.20.030 BUILDINGS.",
      "id": "/us/ca/cities/san-mateo/code/27.20.030",
      "text": "(a) Not more than two buildings designed or used as residences for not more than two families shall be erected, located, or maintained on any one zoning plot. (b) No detached building accessory to a main building shall occupy the portion of any lot in front of the principal building, nor shall any such detached accessory building be less than four feet distant from any other building on the same zoning plot."
    },
    {
      "heading": "27.20.040 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.20.040",
      "text": "Automobile parking facilities shall be provided as required, or permitted, in Chapter 27.64."
    },
    {
      "heading": "27.20.050 MINIMUM DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.20.050",
      "text": "(a) Every one family dwelling hereafter constructed or structurally altered to create an additional dwelling unit shall be on a parcel having a minimum width and area as required in the R1-C districts. (b) Every two family dwelling hereafter constructed shall be on a parcel having the following minimum area: (c) Minimum parcel sizes for special uses shall be at least the same as that prescribed for permitted uses. The planning commission may require additional land area at the time a special use is authorized. (d) All lots located in an R2 district shall have a frontage of not less than thirty (30) feet on a publicly dedicated street as shown on a subdivision map accepted by the City and as recorded in the office of the recorder of San Mateo County, or as designated by a resolution pursuant to Section 17.04.010, unless a permanent easement of access to a public street was of record prior to the effective date of this title, or unless approved pursuant to proceedings authorized by this title. The minimum width of all such parcel shall be not less than thirty (30) feet for a distance of not less than one hundred twenty (120) feet from the frontage property line; provided thereafter the width of the parcel conforms (as to the residue of the parcel) to the required average parcel width requirement of the district wherein the parcel is located."
    },
    {
      "heading": "27.20.060 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.20.060",
      "text": "The floor area ratio of buildings and structures on a zoning plot in this district shall not exceed 0.6."
    },
    {
      "heading": "27.20.065 Maximum Floor Area Ratio (Central Neighborhood & North Central Neighborhood)",
      "id": "/us/ca/cities/san-mateo/code/27.20.065",
      "text": "The floor area ratio of buildings and structures on zoning plots in the R2 district located in the Central Neighborhood and North Central Neighborhood shall not exceed 0.5 for parcels up to 7,500 square feet and 0.6 for parcels greater than 7,500 square feet. \"Central Neighborhood\" for the purposes of this section shall mean the area that is bounded by Highway 92 to the South, the Railroad to the West, Fifth Avenue to the North, and Highway 101 to the East, as shown on the following map. \"North Central Neighborhood\" for the purposes of this section shall mean the area that is bounded by 2nd Avenue to the South, El Camino Real to the West, Poplar Avenue to the North, and Highway 101 to the East, as shown on the following map:  "
    },
    {
      "heading": "27.20.070 YARD AREAS.",
      "id": "/us/ca/cities/san-mateo/code/27.20.070",
      "text": "All regulations of the R1-B district, as to yard areas, shall apply to two family dwellings."
    },
    {
      "heading": "27.20.080 BUILDING HEIGHT AND DAYLIGHT PLANE.",
      "id": "/us/ca/cities/san-mateo/code/27.20.080",
      "text": "All regulations of the R1 district, as to height and daylight plane, shall apply to two family dwellings."
    }
  ],
  "Chapter 27.21 Two-Unit Development Residential Overlay District – R1 Districts": [
    {
      "heading": "Article I Two-Unit Development",
      "id": "/us/ca/cities/san-mateo/code/27.21/I",
      "text": "The purpose of this Article is to allow up to two detached or attached primary housing units on one parcel, establish objective standards, and regulate subdivision of parcels in single-family zoned areas in accordance with state law. This Chapter shall be implemented and interpreted in conjunction with California Government Code Sections 65852.21 and 66411.7, as amended, and applicable objective standards contained within Titles 26 and 27 of the San Mateo Municipal Code. For the purposes of this Chapter, the following definitions apply. Terms not defined herein shall rely upon the definitions contained in Title 26 and Title 27 of the San Mateo Municipal Code. (a) \"Access Corridor\" means an access easement or the 'pole' of a flag lot that provides vehicular access to the right-of-way. Access corridors shall consist of paving and be free of landscaping or other permanent features that obstruct ingress/egress and vehicular traffic to a parcel. (b) \"Acting in concert\" means that the owner, or a person acting as an agent or representative of the owner, knowingly participated with another person in joint activity or parallel action toward a common goal of subdividing the adjacent parcel. (c) \"Car Share Facility\" means one or more parking space(s) that have been designated permanently for car share vehicles, where the vehicles are leased for short periods of time, often by the hour. (d) \"Department\" means the Department of Community Development. (e) \"Existing Exterior Structural Wall\" means and constitutes the original bottom plate and original top plate in its existing position, original studs (with the exception for new window framing), and capable of standing without support. (f) \"Flag or Panhandle Lot\" means a parcel which includes a strip of land that is owned in fee that is used primarily for vehicular access from a public or private street to the major portion of the parcel. For the purposes of determining setbacks, the property line parallel to the primary right-of-way and part of the major portion of the parcel shall be the front property line. Maximum floor area ratio (FAR) shall be based on the gross square footage of the parcel. (g) \"High Quality Transit Corridor\" means a corridor with fixed bus route service with service intervals no longer than 15 minutes during peak commute hours. (h) \"Major Transit Stop\" means a site containing any of the following: (i) an existing rail or bus rapid transit station; (ii) a ferry terminal served by either a bus or rail transit service; or (iii) the intersection of two or more major bus routes with a frequency of service intervals of 15 minutes or less during the morning and afternoon peak commute periods. (i) \"Primary Unit\" (also called a residential dwelling unit or residential unit) means a single-family residence or a residential dwelling unit within a multifamily residential development. A primary unit is distinct from an ADU or junior accessory dwelling unit (JADU), and may be a single-family residence (i.e. one primary unit) or a duplex (i.e. two primary units detached or attached). (j) \"SB 9 Dwelling Unit or SB 9 Unit\" means a primary unit that is developed pursuant to the requirements of this Article, applicable San Mateo Municipal Code provisions, and Government Code Sections 65852.21 and 66411.7, as amended. (k) \"SB 9 Project or SB 9 Planning Application\" means a project application submitted to the City in accordance with this Article, SB 9, and applicable San Mateo Municipal Code provisions to do one or more of the following: (1) Split a qualifying single-family residentially zoned parcel into two lots; or (2) Develop no more than two primary units on a single lot, or (3) When a lot is subdivided, develop no more than two dwelling units, inclusive of ADUs and JADUs, on a single parcel. (l) \"Senate Bill 9 or SB 9\" means the state law signed by the Governor into law on September 19, 2021 that amended Government Code Sections 65852.21 and 66411.7 to allow up to two primary units on and/or lot splits of qualifying single-family zoned parcels. (m) \"Substantial Removal\" means the demolition of 50% or more of a structure's exterior walls (measured in linear feet) and/or roof (measured in square feet). Existing exterior walls that are converted to interior walls shall be counted as walls to be demolished. For the purposes of this Chapter, substantial removal for a roof shall not apply to permit applications for re-roofing where roof pitch alterations do not exceed an increase in height of more than two (2) feet as measured at the highest point or where a SB 9 planning application has been submitted as part of the proposed improvements. Doors, including garage doors, entry doors, and sliding glass doors, shall not be included in the percentage calculation of an existing structure's exterior walls. This section shall not apply to an accessory building or to a residence that has been declared a public nuisance under this Code. (n) \"Sufficient to Allow Separate Conveyance\" means that connected or adjacent units can be sold separately if they conform to condominium standards to allow for the adequate transfer of title, ownership, rights, and interests in the property from one entity to another. (o) \"Urban Lot Split\" means a subdivision of an existing legal single-family zoned parcel into no more than two separate single-family zoned parcels that meet all of the criteria and standards set forth in this Chapter, applicable objective standards of San Mateo Municipal Code Title 26, and Government Code Sections 65852.21 and 66411.7, as amended. Except as otherwise outlined below, the applicable rules of procedure contained in Chapter 27.08 shall apply to all SB 9 planning applications. Where there is a conflict, standards in this Chapter shall prevail. (a) Planning Application Submittal. An SB 9 planning application, on the form(s) prescribed by the Department, for either an attached or detached unit(s) and/or urban lot splits, shall be submitted for all development pursuant to the provisions of this Chapter. (1) An applicant may file concurrent planning applications under this Chapter for one or two-unit development and an urban lot split. (2) Processing of Applications. Unless an SB 9 application is submitted pursuant to Section 27.21.045 of this Chapter, SB 9 application(s) shall be processed as prescribed in Section 27.08.040 of the San Mateo Municipal Code, except that these applications shall be considered ministerially with no public hearing. (b) Informational Notice. Upon receipt of an SB 9 planning application, and once the project is deemed complete, the City shall provide an informational notice that an SB 9 application has been filed with the City to all property owners and tenants within a 500-foot radius of the subject parcel and to the applicable neighborhood association(s) in accordance with the noticing procedures adopted by the Department. (c) Ministerial Permit Approval. If an SB 9 planning application complies with the provisions of this Chapter, a ministerial, non-discretionary permit shall be issued. Notwithstanding anything contrary in this code, the issuance of a ministerial SB 9 Two-Unit Development permit and/or a SB 9 Urban Lot Split permit is not appealable. (d) Submittal Requirements. In addition to the requirements of Section 27.08.010(c), each application shall be accompanied by all of the following: (1) Application Forms. Completed SB 9 planning application forms as prescribed by the Department; (2) Property Ownership. Verification of property ownership in the form of a preliminary title report that is no more than a year old, showing the current owners of the property, the names of record owners of the land, and all existing easements and other reservations, restrictions, or covenants; and (3) Legal Description. An accurate legal description of the property and any resultant lots in the case of an urban lot split application; and (4) Plans. Scaled and accurate plans to include required applicable information as outlined in the Planning Application and/or Urban Lot Split Submittal Requirements checklists; and (5) Affidavit. A completed property owner tenant disclosure affidavit and acknowledgement that the application meets SB 9 eligibility requirements. (6) Findings. Findings of Approval. An SB 9 application not submitted pursuant to Section 27.21.045 of this Chapter shall be approved ministerially if the Zoning Administrator or designee makes all the following findings: (A) The parcel is within the Two-Unit Overlay District and meets all qualifying criteria as outlined in this Chapter; (B) The development meets all applicable objective standards contained in and required by the General Plan, San Mateo Municipal Code or other City adopted plans, policies, or standards; (C) The development does not adversely affect matters regarding police protection, crime prevention, and security because it adheres to the objective standards of Chapter 23.54; (D) The proposed SB 9 unit(s) is consistent with all applicable SB 9 objective design standards of the Two-Unit Overlay District (7) Findings of Denial. An SB 9 application shall be denied if the Building Official makes written findings, based upon a preponderance of evidence, that: (A) The proposed housing development would have a specific adverse impact, as defined and determined in paragraph (2) of subdivision (d) of Section 65589.5, as amended, of the Government Code, upon public health and safety or the physical environment, and for which there is no feasible method to satisfactorily mitigate or avoid the specific adverse impact(s). A deed restriction shall be submitted in a form approved by the City and recorded to run with the land for all development pursuant to this Article as indicated below: (a) Prior to the issuance of any building permit(s), development pursuant to this Chapter shall require a deed restriction to be recorded requiring a prohibition of the establishment of short- term rentals and a requirement that a rental or lease of any dwelling unit created pursuant to this Chapter shall be for a period of at least 30 consecutive days. Projects that do not meet the provisions of this Chapter shall be subject to either a Single-Family Dwelling Design Review (SFDDR) or Site Plan and Architectural Review (SPAR) discretionary review process. (a) In no case shall an application for discretionary review: (1) Propose to increase FAR above that permitted by the underlying zoning district, except to the extent allowed by state law; or (2) Propose to further subdivide a parcel that had been established through a previous urban lot split pursuant to Government Code Sections 65852.21 and 66411.7, as amended; or (3) Propose to increase the maximum number of permitted dwelling units; or (4) Propose a parcel size smaller than 1,200 sq. ft.; or (5) Propose less than one parking space per unit unless otherwise allowed per Section 27.21.070 of this Chapter. The following lands classified as R1-A, R1-B, and R-C are not subject to the Two-Unit Development Overlay District: (a) Any parcel that would require the demolition or alteration of any of the following housing types: (1) Housing that is subject to a recorded covenant, ordinance, or law that restricts rents to levels affordable to persons and families of moderate, low, or very low incomes; or, (2) Housing that is subject to any form of rent or price control through a public entity's valid exercise of its police power; or, (3) Housing that has been occupied by a tenant within the last three years; or, (4) A parcel(s) on which an owner of residential real property has exercised the owner's rights under Government Code Chapter> 12.75 (commencing with Section 7060) of Division 7 of Title 1 (Ellis Act) to withdraw accommodations from rent or lease within 15 years prior to an SB 9 application submittal. (b) On any parcel designated an historic district or property, or located in a resource or hazard area such as high fire areas, wetlands, fault zones, hazardous waste sites or lands under conservation easements per Government Code Sections 65913.4(a)(6)(B-K), as amended. For properties that develop a project pursuant to this overlay, the following limitations apply: (a) A maximum of four units, with a maximum of two primary dwelling units (attached or detached), except as outlined in Article II below. (b) Limitation on Rental. (1) Short Term Rentals Prohibited. No dwelling unit created pursuant to this Chapter shall be rented for a period of less than 30 consecutive days as a short-term rental as set forth in Chapter 5.66. Rentals longer than 30 consecutive days are permitted. (c) Limitation on Sale. (1) If two or more primary units exist on a single parcel, they shall not be sold separately until an urban lot split application has been approved by the City and a final parcel map recorded. (d) Limitation on Use. (1) Lots created pursuant to Article II of this Chapter shall be limited to residential uses only. SB 9 units, as defined in this Chapter, shall comply with the following development standards: (a) Demolition Limits. SB 9 projects that do not involve an urban lot split are subject to the following: (1) Demolition of less than 50% of a structure's exterior structural walls or roof shall be subject to a ministerial review process. (2) Demolition of 50% or more of a structure's exterior structural walls or roof may be permitted subject the Alternative Discretionary Review process listed in Section 27.21.045 of this Chapter and issuance of a Special Use Permit for the substantial removal of the existing structure pursuant to Section 27.18.035 of the San Mateo Municipal Code. (b) Maximum Floor Area Ratio. The maximum Floor Area Ratio (FAR) for all structures on site shall be determined by the underlying zoning district with the following exceptions: (1) Application of development standards of the underlying zoning district shall not preclude the construction of up to two primary dwelling units nor physically preclude either of the two units from being at least 800 square feet in floor area. (2) SB 9 unit(s) in excess of 800 square feet shall be subject to a Single-Family Dwelling Design Review (SFDDR) or Site Plan and Architectural Review (SPAR) discretionary review process and shall be governed by the maximum floor area established by the underlying zoning district. (3) In instances where the existing floor area allowance of a lot has been fully utilized, an SB 9 unit of up to 800 square feet in size with at least 4-foot side and rear yard setbacks and up to 16-feet in height shall be permitted, unless the proposed development would have a specific adverse impact, as defined and determined in paragraph (2) of subdivision (d) of Section 65589.5, as amended, of the Government Code, upon public health and safety or the physical environment, and for which there is no feasible method to satisfactorily mitigate or avoid the specific adverse impact(s). (c) Height. The specific height maximums outlined below are applicable to all zoning districts subject to the Two-Unit Development Overlay District: (1) Attached SB 9 Units. The maximum building height is 24 feet to top of plateline and 32 feet to roof peak as measured from existing grade. (2) Detached SB 9 Units. Maximum building height is 16 feet to top of plateline and 24 feet to roof peak as measured from existing grade. (d) Setbacks. SB 9 unit(s) shall have setbacks as follows: (1) Front Setback. A minimum setback from the front lot line, as required by the lot's underlying zoning district. (2) Side and Rear Setbacks. A minimum setback of four (4) feet shall be required from the side and rear lot lines. (3) No setback shall be required for an existing legally permitted structure that is converted into an SB 9 unit or a structure constructed in the same location and to the same dimensions as an existing legally permitted structure. (e) Parking. (1) General Requirements. There shall be a minimum of one standard size off-street parking space (either uncovered or covered) for each SB 9 unit. All parking, whether required or voluntary, shall be located entirely on the same lot as the dwelling unit it serves and shall conform to the size requirements of the City's \"Standard Drawings and Specifications\" as adopted by resolution of the City Council and on file with the Department of Public Works. Covered parking shall meet all applicable setbacks of the underlying zoning district. (2) Exemptions. No off-street parking shall be required for an SB 9 unit in the following instances: (A) The parcel is located within one-half mile walking distance of a high-quality transit corridor, as defined in Public Resources Code Section 2155(b); as amended; or (B) The parcel is located within one-half mile walking distance of a major transit stop, as defined in Public Resources Code Section 21064.3(e), as amended; or, (C) The parcel is located within one block of a car share facility. (f) Objective Design Standards. (1) New residential construction of primary units subject to streamlined ministerial approval shall comply with the Interim Objective Design Standards as adopted by City Council resolution and as may be amended from time to time by further City Council resolution. (g) Other Development Standards. (1) All development pursuant to this Chapter shall also be subject to the requirements of the California Building Code, Fire Code and local fire sprinkler ordinance requirements. (2) All objective standards of the underlying zoning district, Titles 27 and 23 and other relevant Titles of the San Mateo Municipal Code shall apply. If such standards conflict with this Chapter, the standards in this Chapter shall prevail. In no instance shall any objective building or design standard preclude the development of at least two primary dwelling units of at least 800 square feet each in size, unless the development would have a specific adverse impact, as defined and determined in paragraph (2) of subdivision (d) of Section 65589.5, as amended, of the Government Code, upon public health and safety or the physical environment, and for which there is no feasible method to satisfactorily mitigate or avoid the specific adverse impact(s)."
    },
    {
      "heading": "Article II Urban Lot Splits",
      "id": "/us/ca/cities/san-mateo/code/27.21/II",
      "text": "The purpose of this Article is to implement SB 9, establish objective standards and regulate qualified Urban Lot Splits and development in accordance with state law. Article II shall be implemented and interpreted in conjunction with Article I of this Chapter, California Government Code Sections 65852.21 and 66411.7, San Mateo Municipal Code Chapter 23.40 and Titles 26 and 27, and any other relevant San Mateo Municipal Code section or other City adopted plan. Urban Lot Split Development. In addition to the rules of procedure listed in Section 27.21.030 of Article I above, an Urban Lot Split application shall also conform with the following: (a) Submittal Requirements: (1) Full Site Survey. A full site boundary survey stamped and signed by a Land Surveyor licensed by the State of California. A topographic and boundary survey shall be required for all properties with grades over 15%. (2) Parcel Map. A parcel map pursuant to Title 26 of the San Mateo Municipal Code showing the proposed Urban Lot Split. (3) Affidavit. A completed owner occupancy affidavit and acknowledgement that the property meets Urban Lot Split eligibility requirements outlined in Section 27.21.050 and that the owner of the property intends to occupy one of the housing units as their principal residence for a minimum of three years from the date of the approved Urban Lot Split and recordation of the Final Map. (A) Exception. This requirement shall not apply to an applicant that is a community land trust as defined in clause (ii) of subparagraph (C) of paragraph (11) of subdivision (a) of Section 402.1 of the Revenue and Taxation Code, or if the applicant is a qualified nonprofit corporation as described in Section 214.15 of the Revenue and Taxation Code. (b) Final Parcel Map. Upon an Urban Lot Split application approval, the applicant shall prepare, file, and record a final parcel map with the Department of Public Works pursuant to Article II of Section 26.56 of the San Mateo Municipal Code. (c) Dedications and Improvements. Unless required to accommodate an urban lot split or provide access to a parcel, no dedications of rights-of-ways or the construction of offsite improvements for parcels created pursuant to this Article shall be required as a condition of approval. (d) Findings. To approve an Urban Lot Split application, the Zoning Administrator shall make the findings listed in Section 27.21.030 of Article I above, in addition to the following findings: (1) The parcel being subdivided was not established through a prior SB 9 urban lot split application. (2) The Urban Lot Split conforms to all applicable objective requirements of the Subdivision Map Act (Division 2 commencing with Section 66410), except as otherwise provided in this Section. (3) The parcel being subdivided is not adjacent to another parcel where either the owner of the parcel proposing to be subdivided or any person acting in concert with said owner has previously subdivided the adjacent parcel using the provisions of SB 9. A deed restriction shall be submitted in a form approved by the City and recorded to run with the land for all development pursuant to this Article as indicated below: (a) A prohibition of non-residential uses on any lot created pursuant to this Chapter; (b) A prohibition of the establishment of short-term rentals and a requirement that a rental or lease of any dwelling unit created pursuant to this chapter shall be for a period of at least 30 consecutive days. (c) A prohibition against further subdivision of the parcel using the Urban Lot Split procedures in this Chapter and pursuant to Government Code Section 65852.21 and 66411.7, as amended; The following lands classified as R1-A, R1-B, and R1-C are not eligible for an Urban Lot Split under this Article, if the parcel meets either of the following: (a) Any parcel that was established through prior approval of an Urban Lot Split subdivision as provided for in this Article; or (b) Any parcel proposed to be subdivided that is adjacent to another parcel where either the owner of the parcel proposing to be subdivided or any person acting in concert (as defined in Section 27.21.020(b)) with said owner has previously subdivided the adjacent parcel using the provisions of this Article. Development standards shall be applied to each parcel individually. Each parcel created by an Urban Lot Split shall conform to the Two-Unit Development Standards in Section 27.21.070 and Title 26 of the San Mateo Municipal Code except as otherwise listed below. (a) Demolition. The demolition of 50% or more a structure's exterior structural walls or roof shall require the issuance of a ministerial Special Use Permit for the substantial removal of the existing structure pursuant to the applicable sections of Section 27.18.035 of the Municipal Code. (b) Number of Units. On a lot established through an Urban Lot Split pursuant to Government Code 66411.7, a maximum of two dwelling units shall be allowed per resultant parcel. In no case shall more than two dwelling units on a single lot in any otherwise allowed combination of primary units, SB 9 units, ADUs and/or JADUs be permitted. (c) Parcel Map and Configuration. (1) Number of Parcels. The parcel map shall create no more than two new parcels. (2) Parcel Size. (A) Each newly created parcel shall be of approximately equal areas. The smallest subdivided parcel shall not be less than forty percent (40%) of the lot area of the original parcel proposed for subdivision. (B) Each newly created parcel shall be at least 1,200 square feet in gross area. (d) Access and Driveways. (1) Parcels resulting from an Urban Lot Split shall have access to, provide access to, or adjoin the public right-of-way through their frontage, access corridor, or access easement(s). (A) A minimum 10-foot-wide strip of land owned in fee (i.e. flag lot 'pole') or 10- foot wide access easement shall be provided for all flag lots or landlocked parcels created through an Urban Lot Split. The width of the strip of land owned in fee for flag lots or width of the access easement for landlocked parcels shall not be less than the driveway width requirements of Section 27.64.025. (B) A minimum 20-foot-wide strip of land owned in fee (i.e. flag lot 'pole') or 20- foot wide access easement shall be provided for all flag lots or landlocked parcels created through an Urban Lot Split where the length of the flag lot 'pole' or access easement is greater than 150 feet in length. (2) Access to all new lots and/or units shall be compliant with the San Mateo Consolidated Fire District standard details and specifications for driveways and turnarounds. (3) Easements for the adequate provision of public services and utilities and egress/ingress may be required. (4) Proposed boundary lines shall be free of jogs in alignment, except where physical conditions and established property lines preclude the establishment of straight boundary lines, or such alignment would prohibit the creation of lots pursuant to this Article which are capable of being developed with two residential units that are at least 800 square-feet in size each. (e) Other Development Standards. (1) All development pursuant to this Article shall also be subject to additional development standards as outlined in Section 27.21.070(f) of this Chapter above."
    }
  ],
  "Chapter 27.22 R3 DISTRICT—MULTIPLE FAMILY DWELLINGS (MEDIUM DENSITY)": [
    {
      "heading": "27.22.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.22.010",
      "text": "Use of buildings or land in this district and buildings hereafter erected, structurally altered or enlarged, shall be limited to the following: (a) Any use permitted in the R1 and R2 districts; (b) Multiple family dwellings, as defined in this title; (c) One family row dwellings, as defined in this title; (d) Accessory uses which are necessary to the above-mentioned buildings and uses."
    },
    {
      "heading": "27.22.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.22.020",
      "text": "Unless otherwise provided, the following uses may be allowed if a special use permit is approved: (a) Any special use permitted in the R1 and R2 districts; (b) Bed and breakfast inns; (c) Boarding and lodging houses with a five person limitation; (d) Convalescent homes, rest homes, nursing homes; limited to the housing of not more than six (6) persons in addition to the owner or manager and family; (e) Residential care facility serving seven (7) or more persons in addition to the caregiver, and conforming with the provisions of Chapter 27.27; (f) Day care centers."
    },
    {
      "heading": "27.22.030 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.22.030",
      "text": "Off-street parking facilities shall be provided as required in the off-street parking code (Chapter 27.64)."
    },
    {
      "heading": "27.22.040 MINIMUM DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.22.040",
      "text": "(a) Every dwelling hereafter erected or structurally altered to create one or more additional dwelling units shall be on a parcel having the following minimum development standards: (b) A larger minimum parcel for special uses shall be required by the Planning Commission upon a finding that the minimum parcel area does not adequately accommodate the proposed special use."
    },
    {
      "heading": "27.22.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.22.050",
      "text": "The floor area ratio of buildings and structures on a parcel in this district shall not exceed 0.85, except that the zoning administrator may grant permission to exceed the above maximum floor area ratio, using the procedures outlined for special uses as provided in this title, if the additional floor area will: (1) Not exceed a floor area ratio of 1.0; (2)(A) Be equal to the additional floor area that is required to cover any parking space that is not otherwise required to be covered by provisions of this title, or (B) Is necessary to cover any required turnaround area for required parking, and (C) Increase the livability by providing more usable yard area than could be provided without the permitted increase in floor area."
    },
    {
      "heading": "27.22.055 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.22.055",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.22.060 YARD AREAS GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.22.060",
      "text": "Buildings shall not be erected or enlarged unless the yard areas in the following Sections (27.22.070 through 27.22.090) are provided and maintained in connection with such building, structure or enlargement. Notwithstanding the requirements for front, side, and rear yards (27.22.070 through 27.22.090) and at the City's option, required yards may be combined in various ways to maximize certain locational factors. Such combinations shall be considered by the City as a part of planning application review."
    },
    {
      "heading": "27.22.070 FRONT YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.22.070",
      "text": "(a) A front yard of not less than fifteen feet (15') shall be provided. For buildings exceeding three (3) stories in height, the minimum front yard shall be one-half (1/2) the height of the building, unless a smaller setback is allowed in the granting of a special use permit. On a parcel being developed for multiple-family use, if the front of the parcel abuts an R1 or R2 zoned parcel, the front setback measured from the property line shall be equal to the building height, or fifteen feet (15'), whichever is greater. (b) Garages in Embankments. The same regulations shall apply as in the R1 districts. (c) Private Roads. The same regulations shall apply as in the R1 districts. (d) Subdivision Maps. The same regulations shall apply as in the R1 districts."
    },
    {
      "heading": "27.22.080 SIDE YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.22.080",
      "text": "(a) For one family detached dwellings, the same regulations shall apply as in the R1-B district. (b) For two family dwellings, the same regulations shall apply as in the R2 district. (c) For one and two story multiple family dwellings there shall be provided and maintained a side yard of not less than six feet (6') on each side of the principal building(s). For multiple family dwelling structures of more than two stories in height, the side yard adjacent thereto shall be one-half (1/2) the height of the building to a maximum of twenty-five feet (25') unless a greater dimension is required as a condition of approval for a special use permit. (d) For one and two story multiple family dwellings on corner parcels, there shall be maintained a minimum side yard of not less than seven and one-half feet (7-1/2') on the side adjacent to the street which intersects the street upon which the building maintains frontage. In the case of a reversed corner parcel, there shall be maintained a setback from the side of not less than fifty percent (50%) of the front yard required on the parcels in the rear of such corner parcels but such setback need not exceed ten feet (10'). Accessory buildings on said reversed corner parcel shall not project beyond the front yard requirement on the adjacent parcel to the rear; nor be located nearer than six feet (6') to the side parcel line of said adjacent parcels. For multiple family dwelling structures of more than two (2) stories in height on corner parcels, the minimum required side yard shall be one-half (1/2) the height of the building to a maximum of twenty-five feet (25') unless a greater dimension is required as a condition of approval for special use permits. (e) On a parcel being developed for multiple-family use, if the side of the parcel abuts an R1 or R2 zoned parcel, the side yard setback on that side measured from the property line shall be equal to one-half (1/2) the height of the building, or fifteen feet (15'), whichever is greater. (f) On a parcel improved pursuant to a special use permit with a nonresidential building, exclusive of residential accessory buildings, there shall be a side yard of not less than ten feet (10') on each side of the principal structure. For those nonresidential structures of more than two stories in height, there shall be provided and maintained a side yard setback equal to one-half (1/2) the height of the building, or fifteen feet (15'), whichever is greater. Additional side yard setback may be required as part of the conditions of a special use permit. When a special use is proposed for a parcel which abuts an R1 or R2 zoned parcel, the provisions of subsection (e) shall apply."
    },
    {
      "heading": "27.22.090 REAR YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.22.090",
      "text": "On a parcel upon which a building is constructed there shall be a rear yard setback of not less than fifteen feet (15'). For buildings more than three stories in height, the minimum rear yard shall be one-half (1/2) the height of the building to a maximum of twenty-five feet (25') unless a greater dimension is required as a condition of approval for special use permits. When a parcel zoned for multiple family use abuts an R1 or R2 zoned parcel, the rear yard setback measured from the property line shall be equal to the building height. All required rear yards shall be unobstructed from ground level to the sky, except as otherwise provided in this title."
    },
    {
      "heading": "27.22.095 SPECIAL YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.22.095",
      "text": "Properties from Ninth Avenue south to the City limits which have frontage on El Camino Real shall provide the following yards: (a) A minimum of ten (10) feet along El Camino Real frontage, where property is developed with buildings over two stories in height; (b) One-half (1/2) the height of any building, where the property is adjacent to residential districts."
    },
    {
      "heading": "27.22.097 BUILDING HEIGHT AND SPECIAL YARD REQUIREMENTS—DOWNTOWN SPECIFIC PLAN GATEWAY AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.22.097",
      "text": "Properties within the Gateway area as defined in the Downtown Specific Plan shall conform with the following building height and yard requirements: interior side yard and rear yard setbacks shall conform with sections 27.22.080 and 27.22.090:"
    },
    {
      "heading": "27.22.098 CONFORMANCE WITH GATEWAY DESIGN STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.22.098",
      "text": "All building additions and new buildings within the Gateway area as defined in the Downtown Specific Plan shall conform with the Gateway Design Guidelines."
    },
    {
      "heading": "27.22.100 OPEN SPACE REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.22.100",
      "text": "(a) The open space requirements of this district are in addition to any open space requirements resulting from the approval and filing of a subdivision map, or any open space requirements imposed upon a planned development in accord with the general plan. Open space required by this section is intended to be for the use and enjoyment of the residents of the multiple-family project. (b) Not less than two hundred (200) square feet per bedroom of open parcel area, exclusive of any required off-street parking areas or driveways, shall be provided for the first bedroom in each dwelling unit and at least one hundred (100) square feet per bedroom of open parcel area, exclusive of any required off-street parking areas or driveways, shall be provided for each bedroom after the first bedroom in each dwelling unit. (c) The required open parcel area for each ground floor dwelling unit shall be continuous thereto, and shall have a minimum dimension of not less than ten feet (10') in any direction. Such open parcel area may include the required minimum yard areas set forth in this chapter. Where provision of contiguous open space for ground floor units conflicts with required fire department access, a redistribution of open space may be required, subject to the approval of the fire chief. (d) Open roof decks, balconies, lanais or other open structural areas made a part of the building and improved for outdoor living, may be used to satisfy the open parcel area requirements for each dwelling unit above the ground floor provided that the open roof deck, balcony, lanai, or other open structural area contains a usable area of not less than one hundred (100) square feet and is not less than six feet (6') in any dimension. Required open space for units above the ground floor may be combined for several units and located on the ground. Whether or not required open space is combined, it may be located in whole or in part on the ground, provided that the minimum dimension is ten feet (10') in any direction. Such open space need not be contiguous to the building. (e) The proposed improvement of all required open parcel area (garden patios) or roof decks, balconies, lanais or other structural areas intended for outdoor living shall be designated on plans submitted with planning applications, and upon the approval of such plans shall be considered a required part of the site and structural improvements."
    },
    {
      "heading": "27.22.110 DWELLING STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.22.110",
      "text": "Every multiple family building hereinafter erected or established in a multiple family district, shall provide a minimum floor area for each dwelling unit with or without a kitchen in compliance with the following: The floor area shall be measured from the center of the walls enclosing each dwelling unit, and may include all closet space and storage area contained within the dwelling unit; but shall not include outside patios, balconies, or terraces, or utility rooms used jointly by the occupants."
    }
  ],
  "Chapter 27.24 R4 DISTRICT—MULTIPLE FAMILY DWELLINGS (HIGH DENSITY)": [
    {
      "heading": "27.24.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.24.010",
      "text": "Use of buildings or land in this district and buildings hereafter erected, structurally altered or enlarged, shall be limited to the following: (a) Any use permitted in the R1, R2, or R3 districts; (b) Accessory uses which are necessary to the above-mentioned buildings and uses."
    },
    {
      "heading": "27.24.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.24.020",
      "text": "Unless otherwise provided the following uses may be permitted subject to the approval of a special use permit by the Planning Commission: (a) Any special use permitted in the R3 district; (b) Boarding and lodging houses; (c) Private clubs, lodges, and fraternal organizations including the serving of food and beverages to members and their guests, and including such other facilities customarily provided for the comfort and convenience of the membership. (d) Fraternity and sorority houses; (e) Hospitals and sanitariums, but not including animal hospitals; (f) Philanthropic or eleemosynary uses or institutions, provided that not more than twenty percent (20%) of the gross floor area or two thousand (2,000) square feet, whichever is greater, shall be used as office space. (g) Hotels/motels on existing motel sites along North Bayshore Boulevard from East Popular Avenue to Cypress Avenue."
    },
    {
      "heading": "27.24.030 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.24.030",
      "text": "Off-street parking facilities shall be provided as required in the off-street parking code (Chapter 27.64)."
    },
    {
      "heading": "27.24.040 MINIMUM DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.24.040",
      "text": "(a) Every dwelling hereafter erected or structurally altered to create one or more additional dwelling units shall be on a parcel having the following minimum development standards: (b) A larger minimum parcel for special uses shall be required by the Planning Commission upon a finding that the minimum parcel does not adequately accommodate the proposed special use."
    },
    {
      "heading": "27.24.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.24.050",
      "text": "The floor area ratio of buildings and structures on a parcel in this district shall not exceed 1.5, except that the zoning administrator may grant permission to exceed the above maximum floor area ratio, using the procedures outlined for special uses as provided in this title, if the additional floor area will: (1) Not exceed a floor area ratio of 2.0, (2)(A) Be equal to the additional floor area that is required to cover any parking space that is not otherwise required to be covered by provisions of this title, or (B) Is necessary to cover any required turnaround area for required parking, and (C) Increase the livability by providing more usable yard area than could be provided without the permitted increase in floor area."
    },
    {
      "heading": "27.24.055 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.24.055",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.24.060 YARD AREAS.",
      "id": "/us/ca/cities/san-mateo/code/27.24.060",
      "text": "Unless otherwise provided in this chapter, the regulations in the R3 district shall apply."
    },
    {
      "heading": "27.24.070 DWELLING STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.24.070",
      "text": "Unless otherwise provided in this chapter, the regulations in the R3 district shall apply."
    }
  ],
  "Chapter 27.26 R5 DISTRICT—MULTIPLE FAMILY DWELLINGS (HIGH DENSITY)": [
    {
      "heading": "27.26.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.26.010",
      "text": "Use of buildings or land in this district and buildings hereafter erected, structurally altered or enlarged, shall be limited to the following uses: (a) Any use permitted in the R1, R2, R3 or R4 districts; (b) Accessory uses which are necessary to the above-mentioned buildings and uses."
    },
    {
      "heading": "27.26.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.26.020",
      "text": "Unless otherwise provided the following uses may be permitted subject to the approval of a special use permit by the Planning Commission: (a) Any special use permitted in the R4 district; (b) Apartment hotels; (c) Floor area ratios exceeding 2.0 to a maximum of 3.0."
    },
    {
      "heading": "27.26.030 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.26.030",
      "text": "Off-street parking facilities shall be provided as required in the off-street parking code (Chapter 27.64)."
    },
    {
      "heading": "27.26.040 MINIMUM DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.26.040",
      "text": "(a) Every dwelling hereafter erected or structurally altered to create one or more additional dwelling units shall be on a parcel having the following minimum development standards: (b) A larger minimum parcel for special uses shall be required by the Planning Commission upon a finding that the minimum parcel does not adequately accommodate the proposed special use."
    },
    {
      "heading": "27.26.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.26.050",
      "text": "The floor area ratio of buildings and structures on a zoning plot in this district shall not exceed 2.0 except that the Planning Commission may grant higher floor area ratios for residential high-rise buildings as special uses, but in no case shall the floor area ratio exceed 3.0."
    },
    {
      "heading": "27.26.055 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.26.055",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.26.060 YARD AREAS.",
      "id": "/us/ca/cities/san-mateo/code/27.26.060",
      "text": "The same regulations shall apply as required in the R3 district."
    },
    {
      "heading": "27.26.070 DWELLING STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.26.070",
      "text": "The same regulations shall apply as required in the R3 district."
    },
    {
      "heading": "27.26.080 DEVELOPMENT BONUSES FOR RESIDENTIAL HIGH-RISE BUILDINGS.",
      "id": "/us/ca/cities/san-mateo/code/27.26.080",
      "text": "The planning commission may grant floor area bonuses for the provision of open space in R5 developments if such open space is provided for recreational purposes and is intended to meet the needs of the inhabitants. In determining the suitability of the proposed open space, the following shall be considered: (1) The park and recreation element of the general plan; (2) The composition of the anticipated population of the development; (3) Such other factors and considerations which bear a reasonable relationship to the need for open space. The open space and recreation facilities will be analyzed as part of the required site plan and architectural review (SPAR) and may be granted a bonus by recommendation of the approval body if these facilities are found to meet the recreational needs of the project residents as being adequate in size and number. To earn a floor area bonus for any project feature, a development must earn a bonus from each of the three categories below in this section. In order to earn any bonus provision, a development must include increased natural landscaping. However, not more than twenty-five percent (25%) of natural landscaping in pots or planters shall be counted for the purpose of determining the amount of any floor area bonus. Open space and recreation facilities may be located in required yards under the conditions provided in the open space bonus standards. The following project features may qualify for floor area ratio bonuses when the criteria are met: (1) Outdoor Open Space. Open space bonuses may be granted for provision of natural landscaping, court games and field sports areas as follows: (a) Each two percent (2%) of net parcel area devoted to natural landscaping or water features may be granted a floor area ratio bonus of 0.1, up to a maximum of 0.8. In order to qualify for a bonus, the natural landscaping or water feature must be provided in addition to the required yards and be open to the sky. The minimum bonus required is 0.35. (b) For each court game a floor area ratio bonus of 0.05 may be granted, up to a maximum of 0.1. (c) For each open field sports area, a floor area bonus of 0.05 may be granted, up to a maximum of 0.1. The maximum bonus floor area ratio granted for the provision of exterior open spaces is 1.0. (2) Indoor Recreation Space. Open space bonuses may be granted for provision of recreation room, as follows: For each five-hundred (500) square-foot unit of recreation room floor area, a ratio bonus of 0.05 will be granted to a maximum of 0.2. The maximum bonus floor area ratio for interior open space is 0.2. (3) Open Space and Recreation Special Features. Open space bonuses may be granted for provision of special activity facilities, plazas, and swimming pools as follows: (a) For each exterior special interest activity area, a floor area bonus of 0.05 may be granted, up to a maximum of 0.1. (b) For each exterior plaza area, a floor area bonus of 0.05 may be granted, up to a maximum of 0.1. (c) For an indoor or outdoor swimming pool, a floor area bonus of 0.15 may be granted. For an indoor or outdoor spa, a floor area bonus of 0.05 may be granted. The maximum bonus for swimming pool facilities is 0.2. The maximum bonus for floor area ratio granted for the provision of open space and recreation special features is 0.3."
    }
  ],
  "Chapter 27.27 RESIDENTIAL CARE FACILITIES": [
    {
      "heading": "27.27.010 PURPOSE AND EFFECT OF DEVELOPMENT AND/OR USE PURSUANT TO THIS CHAPTER.",
      "id": "/us/ca/cities/san-mateo/code/27.27.010",
      "text": "This chapter is intended to regulate residential care facilities with seven (7) or more residents in addition to the caregiver. Residential care facilities serving six or fewer residents, in addition to the caregiver, are permitted in all zoning districts that permit single family residences and shall not be required to meet any requirement of this chapter. Any zoning plot developed or used pursuant to this chapter shall not thereafter be used for any purpose other than a residential care facility unless and until the Zoning Administrator has certified in writing that the alternate use satisfies all applicable and then existing land use regulations pertaining to the classification of the zoning plot."
    },
    {
      "heading": "27.27.020 RESIDENTIAL CARE FACILITIES SPECIAL USE CRITERIA.",
      "id": "/us/ca/cities/san-mateo/code/27.27.020",
      "text": "When the proposed use meets the requirements of this chapter and all the following criteria, residential care facilities serving 7 or more residents in addition to the caregiver may be permitted by approval of a special use permit and a site plan and architectural review by the Planning Commission in any zoning district that permits multiple family dwellings, but in no event in an R-1 or R-2 zoning district. (1) There are no other residential care facilities of any size within 300 radial feet of the perimeter of the subject property. (2) Residential occupancy of residential care facilities for the elderly, other than by the caregiver and his or her immediate family, shall be limited to persons over sixty (60) years old or to \"qualified permanent residents\", as defined in California Government Code Sections 51.2-51.4, or any successor legislation, who are provided varying levels and intensities of care and supervision and personal care, and who have voluntarily chosen to reside in this type of group housing arrangement. (3) The proposed use shall be licensed by the State or County and shall be conducted in a manner and with facilities that comply with Title 23 for this kind of occupancy. If the State or County license is suspended or revoked, the special use permit shall automatically also be suspended or revoked. (4) Facilities having persons in excess of 60 years of age or having physical handicaps shall be specifically designed and adapted to include safety bars and rails in bedrooms and bathrooms, ramps, and other provisions required for elderly or handicapped persons by State law or Federal regulations. In addition, such facilities shall include a common dining area as well as adequate common living areas and amenities to facilitate program activities. (5) The use shall be specifically designed and/or maintained to have a residential appearance as determined by review of the Zoning Administrator and be compatible with the architectural character of the zoning district. In residential zoning districts, signs and ramps and any other \"non-residential\" feature visible from the public right-of-way shall not be permitted."
    },
    {
      "heading": "27.27.030 SPECIAL DENSITY STANDARDS FOR RESIDENTIAL CARE FACILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.27.030",
      "text": "Notwithstanding any other provisions of this Code, residential care facilities located in any zoning district that permits community care facilities shall have a total floor area that averages at least 350 square feet of floor area per resident, excluding parking. Where existing structural constraints preclude meeting this requirement, additional floor area to meet this requirement may be achieved through covered patios and decks."
    },
    {
      "heading": "27.27.040 OPEN SPACE REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.27.040",
      "text": "(a) For residential care facilities located outside of the central business district, there shall be a minimum of 100 square feet of common usable open space area per resident and live-in caregiver. (b) For residential care facilities located within the central business district there shall be provided a minimum of 100 square feet of common usable open space area per resident and live-in caregiver. Indoor common living areas and amenities to facilitate program activities may be counted towards this requirement up to a maximum of 75% of the total open space area required. (c) Any open space area to be counted toward the requirements of this Section shall have a minimum dimension of not less than six feet (6') in any direction and be easily accessible to all residents. (d) Outdoor areas shall be designed to provide amenities and recreational areas compatible with the needs of the residents, such as pathways and sitting areas, flower and vegetable gardens, shuffleboard courts, putting greens and similar active recreation areas. (e) Where additional stories prohibit easy access to open space areas on the ground floor, open roof decks, balconies, or lanais shall be provided in an amount, dimension, area, and location as determined to be adequate by the Zoning Administrator. (f) The proposed improvement of all required open space shall be designated on the plans submitted with the planning application, and upon the approval of such plans, be considered a required part of the use permit, site, and structural improvements."
    },
    {
      "heading": "27.27.050 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.27.050",
      "text": "(a) Buildings constructed as residential care facilities serving from seven (7) to fifteen (15) residents shall be required to provide one parking space for each five (5) residents, in addition to one parking space for each live-in caregiver. At least two of the parking spaces shall be enclosed. (b) Buildings constructed as residential care facilities serving more than (15) residents shall be required to provide one parking space for each (5) residents in addition to one parking space for each caregiver, employee, and doctor to be on-site at any one time. (c) Existing single-family residences to be converted into residential care facilities shall maintain existing covered parking; additional parking to meet the requirement of Subsection (a) or (b) above, as applicable, may be enclosed or uncovered."
    },
    {
      "heading": "27.27.060 OTHER LAND USE STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.27.060",
      "text": "Except as expressly provided in this chapter, the land use standards for residential care facilities, such as yard areas and floor area, shall be governed by the land use standards of the applicable zoning district."
    }
  ],
  "Chapter 27.28 DOWNTOWN RESIDENTIAL DISTRICTS": [
    {
      "heading": "27.28.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.28.010",
      "text": "Use of buildings or land shall be limited to uses permitted in R1, R2, R3, or R4 Districts."
    },
    {
      "heading": "27.28.012 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.28.012",
      "text": "Unless otherwise provided, the following uses may be permitted subject to approval of a special use permit by the Planning Commission. (a) Special uses permitted in the R1, R2, R3, and R4 district. (b) Projects with at least fifty (50) dwelling units incorporating: retail bakeries, barber/beauty shops, drug stores, retail dry cleaning/laundry/launderette establishments, a food store or similar convenience goods or personal service uses subject to the following standards: (1) Any non-residential use shall occupy only the ground floor of a residential building; (2) The maximum floor area of all non-residential uses in the project shall not exceed five (5) percent of the building's total floor area or twenty (20) percent of the building's ground floor area, whichever is less. (3) All required parking for non-residential uses shall be permitted only in the rear yards, or in a parking structure which conforms to all building height, bulk and setback requirements; and (4) All non-residential uses shall front on a primary peripheral street as indicated on the Downtown Transportation Plan Map in the Downtown Specific Plan. (c) Boarding and lodging houses."
    },
    {
      "heading": "27.28.014 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.28.014",
      "text": "Off-street parking facilities shall be provided as required in Chapter 27.64 subject to the following design standards: (a) Vehicular access shall not be allowed from any primary peripheral streets unless no other access is available; (b) All open at-grade parking stalls shall be covered with a deck, or trellis, and may be allowed in rear yards only where the maximum rear yard dimension does not abut a street. (c) The area between the perimeter of any at-grade parking facilities and a parcel's boundary lines shall be landscaped as defined in Section 27.04.267 with a minimum depth of six (6) feet, or a minimum depth of three (3) feet if the landscaping is protected from vehicle intrusion by a low decorative wall and/or bollards not exceeding three (3) feet in height, or a combination of the two alternatives."
    },
    {
      "heading": "27.28.016 MINIMUM DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.016",
      "text": "Every dwelling hereafter erected or structurally altered to create one or more additional dwelling units shall meet the following minimum development standards:"
    },
    {
      "heading": "27.28.018 MAXIMUM COVERAGE OF PARCELS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.018",
      "text": "Maximum parcel coverage shall not exceed forty-five (45) percent of the parcel area. The remainder of the parcel shall be landscaped except where parking and access ways are permitted."
    },
    {
      "heading": "27.28.020 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.28.020",
      "text": "The maximum floor area ratio in this district is 3.0."
    },
    {
      "heading": "27.28.022 YARD AREAS GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.28.022",
      "text": "(a) Buildings shall not be erected or enlarged unless the required yard areas are provided and maintained in connection with such building, structure or enlargement. The yards required by this chapter may be combined in various ways with an approved Planned Unit Development to preserve and enhance the existing site elements (including sunlight, protection of existing heritage trees, creeks, waterways, historical or architecturally important sites, or structures, and archaeological sites). Yard combinations shall be considered by the City as a part of the planning application review. (b) For one family and two family dwellings the regulations of the R1-B district shall apply."
    },
    {
      "heading": "27.28.023 BUILDING HEIGHT AND SPECIAL YARD REQUIREMENTS—DOWNTOWN SPECIFIC PLAN GATEWAY AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.28.023",
      "text": "(1) Properties within the Gateway area as defined in the Downtown Specific Plan shall conform with the following building height and yard requirements: interior side yard and rear yard setbacks shall conform with sections 27.28.026 and 27.22.028: (2) Properties outside the Gateway area shall comply with the yard requirements of 27.28.024 through 27.28.028."
    },
    {
      "heading": "27.28.024 FRONT YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.024",
      "text": "Front yards of not less than twenty (20) feet shall be provided and maintained."
    },
    {
      "heading": "27.28.026 SIDE YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.026",
      "text": "Side yards of not less than fifteen (15) feet shall be provided and maintained."
    },
    {
      "heading": "27.28.028 REAR YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.028",
      "text": "Rear yards of not less than twenty-five (25) feet, or twenty-five (25) percent of the parcel's depth, whichever is greater, up to a maximum of forty (40) feet shall be provided and maintained."
    },
    {
      "heading": "27.28.030 LANDSCAPING.",
      "id": "/us/ca/cities/san-mateo/code/27.28.030",
      "text": "At least twenty-five (25) percent of the required rear yard shall be landscaped and planted as defined in Section 27.04.267 for usable open space only (exclusive of parking areas, driveways or accessory facilities) and maintained in common."
    },
    {
      "heading": "27.28.032 USABLE OPEN SPACE REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.032",
      "text": "(a) The open space requirements of this district are in addition to open space requirements resulting from the approval and filing of a subdivision map, or open space required of a planned unit development in accord with the City's general plan or any required off-street parking areas or driveways. Open space required by this section is intended to be for the use and enjoyment of the residents of the development. (b) Each dwelling unit shall be provided with the following: (1) Not less than 100 square feet per dwelling unit of private usable open space directly accessible to each unit provided that no single creditable private usable open space shall be less than eighty (80) square feet or have a dimension of less than eight (8) feet in each direction, or (2) 150 percent of the private usable open space requirement in common usable open spaces provided that no single creditable common usable open space shall be less than 400 square feet with a dimension not less than twenty (20) feet in each direction, or (3) A proportional combination of both of the above."
    },
    {
      "heading": "27.28.034 DWELLING STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.034",
      "text": "Section 27.22.110 in the R3 district shall apply."
    },
    {
      "heading": "27.28.036 CONFORMANCE WITH GATEWAY DESIGN STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.036",
      "text": "All building additions and new buildings within the Gateway area as defined in the Downtown Specific Plan shall conform with the Gateway Design Guidelines."
    },
    {
      "heading": "27.28.040 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.28.040",
      "text": "Use of buildings, or land shall be limited to the uses permitted in R1, R2, R3, R4, R4-D, or R5 Districts."
    },
    {
      "heading": "27.28.042 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.28.042",
      "text": "(1) Special uses allowed in R1, R2, R3, R4, R4-D, or R5 Districts."
    },
    {
      "heading": "27.28.044 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.28.044",
      "text": "Off-street parking facilities shall be provided as required in Chapter 27.64 subject to the design standards in Chapter 27.25 in the R4-D district."
    },
    {
      "heading": "27.28.046 MINIMUM DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.046",
      "text": "Every dwelling hereafter erected or structurally altered to create one or more additional dwelling units shall meet following minimum development standards:"
    },
    {
      "heading": "27.28.048 MAXIMUM COVERAGE OF PARCELS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.048",
      "text": "There is no maximum coverage of parcels in this district."
    },
    {
      "heading": "27.28.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.28.050",
      "text": "The maximum floor area ratio in this district is 3.0."
    },
    {
      "heading": "27.28.052 YARD AREAS GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.28.052",
      "text": "(a) Buildings shall not be constructed or enlarged unless the required yard areas are provided and maintained in connection with such building, structure or enlargement. Yards required by this chapter may be combined in various ways through a planned unit development to preserve and enhance the existing site elements (including sunlight, protection of existing heritage trees, creeks, waterways, historical or architecturally important sites, or structures, and archaeological sites). Yard combinations shall be considered by the City as part of the planning application review. (b) For one family and two family dwellings the regulations of the R1-B district shall apply."
    },
    {
      "heading": "27.28.053 BUILDING HEIGHT AND SPECIAL YARD REQUIREMENTS—DOWNTOWN SPECIFIC PLAN GATEWAY AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.28.053",
      "text": "(1) Properties within the Gateway area as defined in the Downtown Specific Plan shall conform with the following building height and yard requirements: interior side yard and rear yard setbacks shall conform with sections 27.28.056 and 27.22.058:"
    },
    {
      "heading": "27.28.054 CONFORMANCE WITH GATEWAY DESIGN STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.054",
      "text": "All building additions and new buildings within the Gateway area as defined in the Downtown Specific Plan shall conform with the Gateway Design Guidelines."
    },
    {
      "heading": "27.28.056 SIDE YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.056",
      "text": "Side yards of not less than fifteen (15) feet shall be provided and maintained."
    },
    {
      "heading": "27.28.058 REAR YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.058",
      "text": "Rear yards of not less than twenty-five (25) feet shall be provided and maintained."
    },
    {
      "heading": "27.28.060 LANDSCAPING.",
      "id": "/us/ca/cities/san-mateo/code/27.28.060",
      "text": "At least twenty (20) percent of the required rear yard shall be landscaped and planted as defined in Section 27.04.267 for usable open space only (exclusive of parking areas, driveways, or accessory facilities) and maintained in common."
    },
    {
      "heading": "27.28.062 USABLE OPEN SPACE REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.062",
      "text": "(a) The open space requirements of this district are in addition to open space requirements resulting from the approval and filing of a subdivision map, or open space as imposed on a planned development in accord with the City's general plan or any required off-street parking areas or driveways. Open space required by this section is intended to be for the use and enjoyment of the residents of the development. (b) Each dwelling unit shall be provided with the following: (1) Not less than eighty (80) square feet per dwelling unit of private usable open space directly accessible to each unit provided that no single creditable private usable open space shall be less than seventy-five (75) square feet or have a dimension of at least six (6) feet in each direction, or (2) 150 percent of the private usable open space requirement in common usable open spaces provided that no creditable common usable open space shall be less than 300 square feet with a dimension not less than fifteen (15) feet in each direction, or (3) A proportional combination of both of the above."
    },
    {
      "heading": "27.28.064 DWELLING STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.064",
      "text": "Section 27.22.110 in the R3 district shall apply."
    },
    {
      "heading": "27.28.070 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.28.070",
      "text": "Use of buildings, or land in this district and buildings hereafter erected, structurally altered or enlarged shall be limited to the uses permitted in R1, R2, R3, R4, R4-D, R5 or R5-D Districts."
    },
    {
      "heading": "27.28.072 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.28.072",
      "text": "Unless otherwise provided, any special uses permitted in R4, R4-D, R5 or R5-D Districts may be permitted subject to approval of a special use permit by the Planning Commission."
    },
    {
      "heading": "27.28.074 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.28.074",
      "text": "Off-street parking facilities shall be provided as required in Chapter 27.64 subject to the design standards in Section 27.25.030 in the R4-D District."
    },
    {
      "heading": "27.28.076 MINIMUM DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.076",
      "text": "Residential development on properties zoned R6-D shall not exceed 50 units per acre regardless of parcel size."
    },
    {
      "heading": "27.28.078 MAXIMUM COVERAGE OF PARCELS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.078",
      "text": "(a) The maximum coverage of parcels (including enclosed or covered parking) shall be limited to fifty-five percent (55%) of the total parcel area. (b) All areas open to the sky, excluding driveways and accessways, shall be landscaped."
    },
    {
      "heading": "27.28.080 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.28.080",
      "text": "The maximum floor area ratio in this district is 3.0."
    },
    {
      "heading": "27.28.082 YARD AREAS GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.28.082",
      "text": "(a) Buildings shall not be erected or enlarged unless required yard areas are provided and maintained in connection with such building, structure or enlargement. Required yards may be combined in various ways through a planned unit development to preserve and enhance the existing site elements (including sunlight, protection of existing heritage trees, creeks, waterways, historical or architecturally important sites, or structures, and archaeological sites). Such combinations shall be considered by the City as part of the planning application review. (b) For one family and two family dwellings the regulations of the R1-B district shall apply."
    },
    {
      "heading": "27.28.084 FRONT YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.084",
      "text": "A front yard of not less than twenty (20) feet shall be provided and maintained."
    },
    {
      "heading": "27.28.086 SIDE YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.086",
      "text": "A side yard of not less than fifteen (15) feet shall be provided and maintained."
    },
    {
      "heading": "27.28.088 REAR YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.088",
      "text": "A rear yard of not less than twenty-five (25) feet shall be provided and maintained."
    },
    {
      "heading": "27.28.090 LANDSCAPING.",
      "id": "/us/ca/cities/san-mateo/code/27.28.090",
      "text": "At least twenty-five (25) percent of the required rear yard shall be landscaped and planted as defined in Section 27.04.267 for usable open space only (exclusive of parking areas, driveways, or accessory facilities) and maintained in common."
    },
    {
      "heading": "27.28.092 USABLE OPEN SPACE REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.092",
      "text": "(a) The open space requirements of this district are in addition to any open space requirements resulting from the approval and filing of a subdivision map, any open space requirements imposed upon a planned development in accord with the general plan, or any required off street parking areas or driveways. Open space required by this section is intended to be for the use and enjoyment of the residents of the development. (b) Each dwelling unit shall be provided with the following: (1) Not less than eighty (80) square feet per dwelling unit of private open space directly accessible to each unit provided that no single creditable private open space shall be less than seventy-five (75) square feet or have a dimension of less than six (6) feet in each direction, or (2) 150 percent of the private usable open space requirement in common usable open spaces provided that no creditable common usable open space shall be less than 300 square feet with a dimension not less than fifteen (15) feet in each direction, or (3) A proportional combination of both of the above."
    },
    {
      "heading": "27.28.094 DWELLING STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.28.094",
      "text": "Section 27.22.110 in the R3 district shall apply."
    }
  ],
  "Chapter 27.29 RESIDENTIAL OVERLAY DISTRICT—MIXED USE": [
    {
      "heading": "27.29.100 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.29.100",
      "text": "The Residential Overlay District is established to encourage residential development as part of a mixed use development. New residential development is encouraged both to meet housing needs and to provide support for the growth of local businesses."
    },
    {
      "heading": "27.29.102 LANDS SUBJECT TO RESIDENTIAL OVERLAY CLASSIFICATION.",
      "id": "/us/ca/cities/san-mateo/code/27.29.102",
      "text": "The /R, /R4, and /R5 classifications may be superimposed only on those lands classified E or C (except C4)."
    },
    {
      "heading": "27.29.103 R6-D STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.29.103",
      "text": "Notwithstanding other provisions of this section, when any /R property is developed in conjunction with an abutting R6-D, all requirements of the R6-D zone shall apply."
    },
    {
      "heading": "27.29.104 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.29.104",
      "text": "In this overlay district, residential use may be permitted as either a principal use or as part of a mixed use project, provided that in C zones within the area encompassed by the Downtown Specific Plan, residential uses shall be permitted only above the first floor level."
    },
    {
      "heading": "27.29.106 DENSITY.",
      "id": "/us/ca/cities/san-mateo/code/27.29.106",
      "text": "(a) The maximum allowed density shall be as follows: (1) In /R4 districts, the development standards in Section 27.24.040 shall apply; (2) In /R5 districts, residential development shall not exceed 50 units per acre, regardless of parcel size; (3) In /R districts, the following minimum development standards shall apply: (A) For parcels located within the Downtown Specific Plan area, residential development shall not exceed 50 units per acre, regardless of parcel size. Densities above 50 units per acre are permitted only where specific criteria are met as stated in the General Plan Land Use Element. (B) For parcels located outside the Downtown Specific Plan Area, the following minimum standards shall apply: (b) A larger minimum parcel for special uses shall be required by the Planning Commission upon a finding that the minimum parcel does not adequately accommodate the proposed special use."
    },
    {
      "heading": "27.29.108 MAXIMUM COVERAGE OF PARCELS.",
      "id": "/us/ca/cities/san-mateo/code/27.29.108",
      "text": "Maximum parcel coverage shall not exceed the standards of the underlying zoning district."
    },
    {
      "heading": "27.29.110 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.29.110",
      "text": "Residential development may exceed the floor area ratio of the underlying district provided that the maximum floor area ratio, including the residential overlay, shall not exceed the following: (a) In /R4 districts, the maximum floor area ratio shall not exceed 2.0; (b) In /R5 districts, the maximum floor area ratio shall not exceed 3.0; (c) In /R districts, the maximum floor area ratio shall not exceed the standards of the underlying zoning district or floor area ratio range of the residential overlay district as delineated on the Building Intensity Plan of the General Plan."
    },
    {
      "heading": "27.29.112 MAXIMUM HEIGHT AND BULK.",
      "id": "/us/ca/cities/san-mateo/code/27.29.112",
      "text": "Maximum height and bulk standards shall be as follows: (a) Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan. (b) For parcels located within the area encompassed by the Downtown Specific Plan, the bulk of all buildings shall not exceed the standards set forth in Chapter 27.40 Building Height and Bulk District for Downtown."
    },
    {
      "heading": "27.29.114 USEABLE OPEN SPACE REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.29.114",
      "text": "Section 27.28.062, Subsection (b) in the R5-D district shall apply."
    },
    {
      "heading": "27.29.116 SETBACKS AND YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.29.116",
      "text": "For mixed use projects, yard or setback requirements of the underlying zone shall apply. For projects involving only residential use, the following requirements shall apply: (a) In /R, /R4 and /R5 districts, the setback requirements in the R3 district shall apply; (b) In CBD/R districts, the setback requirements in the CBD district shall apply."
    },
    {
      "heading": "27.29.118 THIRD AND FOURTH AVENUE SETBACK REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.29.118",
      "text": "A landscape buffer of at least 20 feet and not more than 25 feet shall be provided along Third and Fourth Avenues from U.S. 101 to South Delaware Street. Only paving required for vehicular and pedestrian entrances shall be permitted; no parking shall be permitted in the setback. The building line shall commence at a distance of not more than 25 feet from the property line along 3rd and/or 4th Avenues."
    }
  ],
  "Chapter 27.30 C1 DISTRICTS—NEIGHBORHOOD COMMERCIAL": [
    {
      "heading": "27.30.005 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.30.005",
      "text": "The Neighborhood Commercial District is intended to create and maintain neighborhood shopping areas under standards that provide for compatibility with surrounding residential areas. Uses include retail sales serving the immediate neighborhood, limited office space, and personal services."
    },
    {
      "heading": "27.30.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.30.010",
      "text": "The following uses are permitted provided that the use limitations contained in Section 27.30.025, \"Permitted and special uses—Twenty-Fifth Avenue Improvement Area,\" shall apply to properties in the Twenty-Fifth Avenue Improvement Area and the use limitations contained in Section 27.30.027, \"Permitted and special uses—Hillsdale Station Area Plan Active Zone,\" shall apply to properties in the Hillsdale Station Area Plan Active Zone: (a) Permitted Uses in Residential Districts. Residential units only on parcels designated with a residential overlay district classification subject to R3 district \"Minimum Development Standards\" in Section 27.22.040 and affordable housing requirements as adopted by City Council resolution, unless otherwise specified in Chapter 27.29; however, secondary units are prohibited; (b) Animal grooming, provided no overnight boarding occurs on the site; (c) Bakeries; (d) Barber shops and hair salons; (e) Delicatessens; (f) Dry cleaners, with customer service areas; (g) Financial institutions, provided the ground floor area devoted to this use does not exceed 2,500 square feet per establishment; (h) Health studios and spas; (i) Laundromats; (j) Libraries; (k) Newspaper publishing; (l) Offices, provided the ground floor area devoted to this use does not exceed 2,500 square feet per establishment; (m) Photo processing; (n) Picture framing; (o) Real estate establishments; (p) Restaurants and accessory outdoor dining areas, without drive-through facilities; (q) Retail uses, such as, but not limited to, the following uses, subject to a maximum of 15,000 square feet of floor area per establishment except for supermarkets and drug stores: (1) Antique shops, (2) Apparel sales, tailoring and repair stores, (3) Drug stores, (4) Hardware and garden supply stores, (5) Household furnishings, (6) Pet shops, (7) Supermarkets and grocery stores; (r) Reverse vending machines, subject to regulations established in Chapter 27.69; (s) Schools and day care facilities; (t) Travel agencies; (u) Accessory uses to principle uses permitted; and (v) Other compatible uses as determined by the zoning administrator."
    },
    {
      "heading": "27.30.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.30.020",
      "text": "The following uses may also be permitted subject to approval of a special use permit, provided that the use limitations contained in Section 27.30.025, \"Permitted and special uses—Twenty-Fifth Avenue Improvement Area,\" shall apply to properties in the Twenty-Fifth Avenue improvement Area and the use limitations contained in Section 27.30.027, \"Permitted and special uses—Hillsdale Station Area Plan Active Zone,\" shall apply to properties in the Hillsdale Station Area Plan Active Zone: (a) Accessory buildings containing plumbing; (b) Alternative financial services subject to the following requirements: (1) A maximum of four alternative financial services may be located in the City of San Mateo. (2) No alternative financial service may be located within a radius of 1,000 feet from the nearest existing alternative financial service. (3) Any alternative financial service seeking to begin operations after the effective date of the ordinance codified in this section shall meet the following minimum standards of performance, which shall be included as conditions of approval for such uses: (i) A lighting plan shall be reviewed and approved by the Police Department and the Building Division for conformance with the City's security ordinance prior to the issuance of building permits. (ii) Storefronts shall have glass or transparent glazing in the windows and doors. No more than 10% of any window or door area shall be covered by signs, banners, or opaque coverings of any kind. (iii) Hours of operation shall be limited to 7:00 a.m. to 7:00 p.m. (iv) At least one uniformed security guard will be on duty at all times the business is open. The security guard shall patrol the interior and all exterior portions of the property under the control of the owner or operator of the alternative financial service, including, but not limited to, parking lots and any open public spaces such as lobbies. (c) Automobile gasoline service stations; (d) Boarding, lodging, or rooming houses; (e) Community care facilities serving seven or more persons in addition to the caregiver, and conforming with the provisions of Chapter 27.27; (f) Convalescent homes, rest homes, nursing homes, limited to the housing of not more than six persons in addition to the owner or manager, and family; (g) Drive-through facilities for financial institutions and for pharmacies dispensing only prescriptions or medicinal goods at the drive-through facility. Drive-through facilities for pharmacies shall be subject to the parking requirements for financial institution drive-through uses, as enumerated in Section 27.64.160(7)(a). (h) Fast food establishments without drive-through facilities; (i) Financial institutions, exceeding 2,500 square feet of ground floor area per establishment up to a maximum of 15,000 square feet of floor area; (j) Offices exceeding 2,500 square feet of ground floor area per establishment up to a maximum of 15,000 square feet of floor area; (k) Parking facilities, as a principal use; (l) Public utility and public service uses; (m) Recreational vehicle storage, subject to regulations established in Section 27.64.267, and only on those parcels designated for such use in Section 27.60.180; (n) Recycling facilities subject to regulations established in Chapter 27.69; (o) Religious institutions; (p) Residential units on parcels without a residential overlay district classification subject to R3 district \"Minimum Development Standards\" in Section 27.22.040 and affordable housing requirements as adopted by City Council resolution, unless otherwise specified in Chapter 27.29; however, secondary units are prohibited; (q) Businesses selling or renting firearms as defined by Penal Code Section 12001(b); and (r) Other compatible uses as determined by the zoning administrator subject to the granting of a special use permit."
    },
    {
      "heading": "27.30.025 PERMITTED AND SPECIAL USES—TWENTY-FIFTH AVENUE IMPROVEMENT AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.30.025",
      "text": "All permitted uses set forth in Section 27.30.010 and special uses set forth in Section 27.30.020 shall be permitted in the Twenty-Fifth Avenue Improvement Area, as shown on Exhibit A, with the following qualifications: (a) Permitted Uses. (1) Financial institutions, provided the ground floor area devoted to this use does not exceed 2,500 square feet per building; and that such uses are retail service in nature, dedicated to serving the general customer, and not open by appointment only. At least 50% of the ground floor area shall be devoted to this type of retail, customer serving use; (2) Offices, including, but not limited to, architectural, contractor, and real estate sales operations, travel agencies, and medical and dental offices that are neighborhood serving in nature; and provided the ground floor area devoted to this use does not exceed 2,500 square feet per building; and (3) Accessory uses to principle uses permitted; including a maximum of 15% of floor area for ancillary office uses related to retail establishments located in the ground floor area of the district, and which are not visible from the street nor located within the retail storefront area. (b) Special Uses, subject to approval of a Special Use Permit. (1) Financial institutions, subject to the use restrictions listed in subsection (a)(1) above, exceeding 2,500 square feet of ground floor area per building up to a maximum of 15,000 square feet of floor area per building; and (2) Offices including, but not limited to, architectural, contractor, and real estate sales operations, travel agencies, and medical and dental offices that are neighborhood serving in nature, exceeding 2,500 square feet of ground floor area per building up to a maximum of 15,000 square feet of floor area per building. All ground floor uses, including permitted and special uses set forth in subsections (a) and (b) above, shall maintain visibility of their retail, office, or lobby space from the street, allow for service of patrons on an unannounced or drop-in basis, and maintain retail storefronts comparable to traditional retail sales operations, including display of goods and services for sale."
    },
    {
      "heading": "27.30.027 PERMITTED AND SPECIAL USES—HILLSDALE STATION AREA PLAN ACTIVE ZONE.",
      "id": "/us/ca/cities/san-mateo/code/27.30.027",
      "text": "All permitted uses set forth in Section 27.30.010 and special uses set forth in Section 27.30.020 shall be permitted in the Hillsdale Station Area Plan Active Zone, as shown on the map that follows, except that ground floor residential uses are not permitted in the portion of parcels that face onto 25th Avenue or in the first 30 feet of depth of a building facing El Camino Real, with the following exceptions: (a) Affordable Housing. Projects that are 100% affordable to very low, low, or moderate income households, or designated as 100% for senior households, as defined in Chapter 27.15, \"Density bonus.\" (b) Ancillary Uses. Residential entryways, lobbies, and other ancillary uses related to residential uses, so long as they are not the primary use of the ground floor facing El Camino Real. (c) Large Parcels. For parcels with more than 300 feet of frontage along El Camino Real, a minimum of 50% of the parcel frontage (measured in linear feet) must meet this requirement. "
    },
    {
      "heading": "27.30.030 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.30.030",
      "text": "All uses except residences shall be subject to the following conditions: (a) Manufacturing, processing, or treatment of products other than which is clearly incidental and essential to the retail business shall not be conducted on the same premises; (b) No use shall generate odor, dust, smoke, noise, vibration, toxic waste, or other emissions which constitute nuisances; (c) Exterior signs displayed shall pertain only to a use conducted within the building; (d) Uses including storage of equipment, materials, supplies, and commercial vehicles for off-site business shall be conducted wholly within an enclosed building, except as permitted or as authorized by special use permit."
    },
    {
      "heading": "27.30.040 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.30.040",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64."
    },
    {
      "heading": "27.30.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.30.050",
      "text": "The maximum floor area ratio of buildings and structures on a zoning plot shall be as follows: (a) In a C1-.5 district, the floor area ratio shall not exceed 0.5; (b) In a C1-1 district, the floor area ratio shall not exceed 1.0; (c) In a C1-1.5 district, the floor area ratio shall not exceed 1.5; (d) In a C1-2 district, the floor area ratio shall not exceed 2.0; (e) In a C1-3 district, the floor area ratio shall not exceed 3.0."
    },
    {
      "heading": "27.30.055 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.30.055",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.30.060 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.30.060",
      "text": "(a) C1 districts which adjoin residential districts shall provide buffers as follows: (1) Front Yards. Parcels fronting on a street, opposite a residential district, wherein 80% or more of the lots, between two intersecting streets, are in a residential district, the commercial parcel shall provide a front yard pursuant to the requirement of the residential district. In a case where multiple residential districts are involved, the most restrictive district standards shall apply. The extension of a front or side parcel line coinciding with a residential district front parcel line shall provide a front yard pursuant to the requirements of the residential district. The yard shall extend a distance of 25 feet from the residential district parcel line, including the width of intervening alleys, drainage channels, or similar facilities. (2) Side Yards. Side parcel lines coinciding with a residential district side or rear parcel line, shall provide a side yard pursuant to the requirements of the residential district. (3) Rear Yards. Rear parcel lines coinciding with a residential district side parcel line shall provide a side yard pursuant to the side yard requirements of the residential district. In a case where multiple residential districts are involved the most restrictive district standards shall apply. Rear parcel lines coinciding with a residential district rear parcel line shall provide a minimum rear yard of 10 feet. (4) All Yards. Yards shall be unobstructed from the ground level to the sky. (5) Required Walls or Fences. A solid wall or solid fence is required for parcels abutting residential districts as provided in Section 27.84.030. (b) Fast-food establishments which sell fast foods shall be separated from each other and from residential districts by at least 100 feet, measured from the nearest parcel lines. Fast food establishments may be closer than 100 feet when located in a shopping center. (c) Special Districts. Parcels adjacent to the shoreline or an open space district, shall provide a minimum yard of 15 feet.  "
    },
    {
      "heading": "27.30.070 SETBACKS AND BUILD-TO-LINE STANDARDS FOR EL CAMINO REAL.",
      "id": "/us/ca/cities/san-mateo/code/27.30.070",
      "text": "(a) Setbacks. (1) Properties from Ninth Avenue to SR 92 which have frontage on El Camino Real shall provide the following yards: (i) A minimum of 10 feet from front of property line along El Camino Real Frontage where property is developed with buildings over two stories in height; and (ii) One-half the height of any building where the property is adjacent to residential districts. (2) Properties with frontage on El Camino Real from SR 92 to the Belmont City limits shall provide the following yards: (i) A minimum of 10 feet from back of curb along the El Camino Real Frontage where property is developed with parking lots and/or buildings up to two stories and/or 28 feet in height from grade of sidewalk; (ii) Buildings over two stories and/or 28 feet in height from grade of sidewalk, shall be set back a minimum of 10 feet from the property line along the El Camino Real Frontage; and (iii) Where the property is adjacent to residential districts, buildings over two stories and/or 28 feet in height from grade of sidewalk, shall be set back one-half the height of the building along the El Camino Real frontage; and (iv) Corner properties along El Camino Real shall provide setbacks indicated in subsection (a)(2)(i) through (iii) along the side street frontages for a minimum of 50% of property frontage measured from the corner of the intersection. (v) Entry features and/or entry towers above two stories and/or 28 feet in height from the grade of the sidewalk are allowed to extend up to the setbacks indicated in subsection (a)(2)(i) for properties along El Camino Real.   (b) Build-to-line for properties with frontage on El Camino Real from SR 92 to the Belmont City limits shall be as follows: (1) Buildings shall be built to the setback line indicated in subsection (a) for a minimum of 50% of the frontage on El Camino Real. The building shall be contiguous along the build-to-line, although the building facade(s) may be articulated; (2) Buildings on corner parcels shall be built to the corner along the setback line indicated in subsection (a) for a minimum of 50% of the frontage on El Camino Real and shall continue the minimum setback line in subsection (a) for at least 50% of side street frontage. In case of parcels with depth less than 100 feet, the 50% build-to-line along the side street may be reduced to accommodate necessary parking access from the side street; and (3) Up to 25% of the building may be set back further from the required build-to-line indicated in subsection (b)(1) to provide for a public amenity such as a plaza, outdoor seating or outdoor dining. In no case shall the setback be greater than 20 feet from the back of curb or 10 feet from the property line along El Camino Real, whichever is greater. (c) Setback and build-to-line for Q5 (Qualified Overlay District 5) setbacks and build-to-lines set forth in subsections (a) and (b) may be modified in accordance with findings as provided for in Section 27.60.160(e). "
    }
  ],
  "Chapter 27.32 C2 DISTRICTS—REGIONAL/COMMUNITY COMMERCIAL": [
    {
      "heading": "27.32.005 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.32.005",
      "text": "The Regional/Community Commercial District is intended to create and maintain major commercial centers accommodating a broad range of office, retail, and personal services of community-wide or regional significance."
    },
    {
      "heading": "27.32.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.32.010",
      "text": "The following uses are permitted: (a) Permitted uses in the C1 district; (b) Art galleries; (c) Automotive accessory stores, excluding on-site service and repair of vehicles; (d) Boarding, lodging, or rooming houses; (e) Catering services; (f) Hotels and motels, including restaurant and meeting rooms; (g) Laundries; (h) Medical and dental clinics, including laboratories; (i) Offices; (j) Parking facilities; (k) Printing, lithographing, or publishing establishments for newspaper, business cards, and other similar uses; (l) Radio and television broadcasting stations; (m) Reproduction services; (n) Residential units, only on parcels designated with a Q5 overlay classification or a residential overlay district classification, subject to R4 district \"Minimum Development Standards\" in Section 27.24.040 and affordable housing requirements as adopted by City Council resolution, except as otherwise specified in Chapter 27.29; however, secondary units are prohibited; (o) Retail uses, including incidental rental and repair; (p) Emergency Shelters, located more than 300 feet from single family zoning districts; (q) Accessory uses to principle uses permitted; and (r) Other compatible uses as determined by the zoning administrator."
    },
    {
      "heading": "27.32.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.32.020",
      "text": "The following uses may also be permitted, subject to approval of a special use permit: (a) Special uses permitted in the residential and C1 districts, except increases in floor area ratios; (b) Clubs, lodges, and fraternal organizations; (c) Commercial recreation uses; (d) Hospitals; (e) Mortuaries; (f) Public transportation facilities and terminals; and other similar uses; (g) Residential units on parcels without a residential overlay district classification subject to R4 district \"Minimum Development Standards\" in Section 27.24.040 and affordable housing requirements as adopted by City Council resolution, unless otherwise specified in Chapter 27.29; however, secondary units are prohibited; (h) Recreational vehicle storage, subject to the provisions of Section 27.64.267 of this Title; (i) Theaters, excluding drive-in theaters; and (j) Other compatible uses as determined by the zoning administrator subject to the granting of a special permit."
    },
    {
      "heading": "27.32.030 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.32.030",
      "text": "All uses, except residences, shall be subject to the following conditions; (a) Manufacturing, processing, or treatment of products which is clearly incidental and essential to the retail business may be conducted on the same premises; (b) Uses shall not generate odor, dust, smoke, noise, vibration, toxic wastes or other emissions which constitute nuisances; (c) Exterior signs shall pertain only to a use conducted within the building; (d) Uses shall be conducted wholly within an enclosed building, except as authorized by special use permit, or as previously authorized, or if the use is legally non-conforming."
    },
    {
      "heading": "27.32.040 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.32.040",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64."
    },
    {
      "heading": "27.32.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.32.050",
      "text": "The maximum floor area ratio of buildings and structures on a zoning plot shall be as follows: (a) In a C2-.5 district, the floor area ratio shall not exceed 0.5; (b) In a C2-.62 district, the floor area ratio shall not exceed 0.62; except Fashion Island Shopping Mall property may have floor area ratios of 1.0 for office and hotel uses, and 2.0 for residential uses provided traffic generated from these uses does not exceed traffic generated from retail uses with a 0.62 floor area ratio. Covered parking for office use shall not be counted as floor area on the Fashion Island Shopping Mall site. (c) In a C2-1 district, the floor area ratio shall not exceed 1.0; (d) In a C2-2 district, the floor area ratio shall not exceed 2.0."
    },
    {
      "heading": "27.32.055 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.32.055",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.32.060 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.32.060",
      "text": "In the C2 Districts, the regulations governing buffers in the C1 districts shall apply."
    },
    {
      "heading": "27.32.070 SETBACK AND BUILD-TO-LINE STANDARDS FOR EL CAMINO REAL.",
      "id": "/us/ca/cities/san-mateo/code/27.32.070",
      "text": "The regulations governing setback and build-to-line standards for El Camino Real in the C1 districts shall apply."
    }
  ],
  "Chapter 27.34 C3 DISTRICTS—REGIONAL/COMMUNITY COMMERCIAL": [
    {
      "heading": "27.34.005 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.34.005",
      "text": "The Regional/Community Commercial District is intended to create and maintain major commercial centers accommodating a broad range of office, retail, and service uses of community-wide or regional significance. The C3 District differs from the C2 District in that a broader range of uses are allowed in the C3 District."
    },
    {
      "heading": "27.34.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.34.010",
      "text": "The following uses are permitted: (a) Permitted uses in the C1 and C2 districts; however, secondary units are prohibited; (b) Ambulance service; (c) Automobile, boat, and truck sales and rental, including service and repair as accessory to the primary sales use, sales may occur on open lot; (d) Automobile service, parts, and repairs, classified as minor motor vehicle repair in Section 27.04.325; (e) Car wash and detailing facilities, may not occur on open lot; (f) Laboratories, research, experimental, and testing, provided no production or manufacturing of products occurs on the premises; (g) Accessory uses to principle uses permitted; and (h) Other compatible uses as determined by the Zoning Administrator."
    },
    {
      "heading": "27.34.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.34.020",
      "text": "The following uses may also be permitted, subject to approval of a special use permit: (a) Special uses permitted in the C1 and C2 districts; (b) Auditorium, stadium, arena, armory, gymnasium, and other similar uses for public events; (c) Restaurants, with drive-thru facilities; and (d) Other compatible uses as determined by the Zoning Administrator subject to the granting of a special permit."
    },
    {
      "heading": "27.34.030 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.34.030",
      "text": "All uses permitted in this district shall be retail or service establishments dealing directly with consumers and shall be subject to the following conditions: (a) That there shall be no manufacturing, processing or treatment of products other than those which are clearly incidental and essential to the retail business conducted on the same premises; (b) That all permitted uses in this district be conducted without objection from adjoining users due to odor, dust, smoke, noise, vibration, or other similar cause; (c) That any exterior sign displayed shall pertain only to a use conducted within the building; (d) All uses permitted under this chapter shall be conducted wholly within an enclosed building, except as may be specifically authorized by special permit."
    },
    {
      "heading": "27.34.040 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.34.040",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64."
    },
    {
      "heading": "27.34.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.34.050",
      "text": "The floor area ratio of all buildings and structures on a zoning plot shall be as follows: (a) In a C3-1 district, the floor area ratio shall not exceed 1.0; (b) In a C3-2 district, the floor area ratio shall not exceed 2.0."
    },
    {
      "heading": "27.34.055 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.34.055",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.34.060 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.34.060",
      "text": "The regulations governing buffers in the C1 districts shall also apply in the C3 districts."
    },
    {
      "heading": "27.34.070 SETBACK AND BUILD-TO-LINE STANDARDS FOR EL CAMINO REAL.",
      "id": "/us/ca/cities/san-mateo/code/27.34.070",
      "text": "The regulations governing setback and build-to-line standards for El Camino Real in the C1 districts shall apply."
    }
  ],
  "Chapter 27.36 C4 DISTRICTS—SERVICE COMMERCIAL": [
    {
      "heading": "27.36.005 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.36.005",
      "text": "The purpose of the service commercial district is to create and maintain a broad range of city-wide and regional service uses including major automobile and truck repair, construction materials yards, and limited processing of materials."
    },
    {
      "heading": "27.36.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.36.010",
      "text": "The following uses are permitted: (a) Permitted uses in the C1, C2, and C3 districts, except that residential uses, office uses on the properties along Palm Avenue between Twentieth and Twenty-fifth Avenues, secondary units, and emergency shelters are prohibited; (b) Air conditioning and heating sales and service; (c) Animal hospitals, which may include outdoor kennels; (d) Automobile parts, service, and repair classified as major motor vehicle repair in Section 27.04.320; (e) Construction materials sales and lumber yards; (f) Dry cleaning establishments, without customer service area; (g) Linen, towel, diaper, and other similar supply services; (h) Machinery sales, rental, and service, when conducted within an enclosed building; (i) Parcel delivery and receiving stations; (j) Processing and assembly of goods determined by the Zoning Administrator to be compatible with adjacent uses, provided that space in a building does not exceed six thousand square feet of total floor and basement space, not including stairwells or elevator shafts; and provided such processing or assembly can be conducted without noise, vibration, odor, dust, or any other condition which might be disturbing to occupants of adjacent buildings. When manufacturing operations of the same or similar products demand space exceeding six thousand square feet, they shall be located in the M1 district. (k) Sheet metal shops; (l) Storage and warehousing; (m) Tool, die, and pattern making; (n) Welding and iron work; (o) Wholesale establishments; (p) Accessory uses to principle uses; and (q) Other compatible uses as determined by the Zoning Administrator."
    },
    {
      "heading": "27.36.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.36.020",
      "text": "The following uses may also be permitted if their site locations and proposed development plans are first approved as provided in Chapters 27.06 through 27.12, 27.62, 27.74, 27.78 and 27.80: (a) Any of the special uses permitted in the C1, C2 or C3 districts, except that residential uses and secondary units are prohibited; (b) Fuel bulk station (flammable liquids) subject to the regulations of Chapter 23.28; (c) Storage of impounded motor vehicles on an open lot."
    },
    {
      "heading": "27.36.030 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.36.030",
      "text": "Permitted uses and special uses in the C4 districts are subject to the following conditions: (a) All activities involving the production, processing, cleaning, servicing, testing or repair of materials, goods or products shall conform with the performance standards established for the M1 district in Chapter 27.56; (b) All production, processing, assembly, cleaning, servicing, testing or repair of materials, goods or products shall take place within completely enclosed buildings unless otherwise indicated herein. Storage of fuel, building materials, equipment, and all other storage, except for parked motor vehicles and retail and display of construction materials, shall take place within enclosed buildings; (c) All parked and impounded motor vehicles in an open lot shall have such lot completely enclosed by a solid wall or solid fence, including doors or gates thereto, not less than six feet in height. All such motor vehicles shall be parked or placed in an orderly manner within such fenced lot with clear and adequate passageways to allow free and unobstructed access and movement of the fire department in case of fire. The manner of handling and keeping impounded motor vehicles shall, at all times, be subject to the approval of the chiefs of the police and fire departments; (d) Such conditions relating to noise emissions, lighting and hours of operation that are reasonably necessary in the interests of the public health, welfare and safety; (e) When granting a special permit for the storage of impounded motor vehicles, the Planning Commission shall specify the expiration date of said permit and the conditions to be met for its renewal, and may specify periodic reviews thereof. (f) All uses permitted under this chapter shall be conducted wholly within an enclosed building except as may be specially authorized by special permit."
    },
    {
      "heading": "27.36.040 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.36.040",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64."
    },
    {
      "heading": "27.36.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.36.050",
      "text": "The maximum floor area ratio of all buildings and structures on a zoning plot shall be as follows: (a) In a C4-.5 district, the floor area ratio shall not exceed 0.5; (b) In a C4-1 district, the floor area ratio shall not exceed 1.0. (c) In a C4-1.5 district, the floor area ratio shall not exceed 1.5."
    },
    {
      "heading": "27.36.055 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.36.055",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.36.060 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.36.060",
      "text": "The regulations governing buffers in the C1 district shall also apply to the C4 district."
    },
    {
      "heading": "27.36.070 SETBACK AND BUILD-TO-LINE STANDARDS FOR EL CAMINO REAL.",
      "id": "/us/ca/cities/san-mateo/code/27.36.070",
      "text": "The regulations governing setback and build-to-line standards for El Camino Real in the C1 districts shall apply."
    }
  ],
  "Chapter 27.38 CBD DISTRICTS—CENTRAL BUSINESS DISTRICT": [
    {
      "heading": "27.38.010 PURPOSE—INTENT.",
      "id": "/us/ca/cities/san-mateo/code/27.38.010",
      "text": "(a) The purpose of the CBD District is to encourage the development and re-use of existing downtown structures as a center for retail, cultural, entertainment, and community service uses. Pedestrian activity should be strongly encouraged at the ground floor level, while upper floor office and residential uses should be encouraged to promote active daytime and nighttime use of the downtown area. Amenities that will enhance the downtown environment for public and public oriented uses shall also be encouraged. (b) In order to insure that these purposes will be carried out, a basic set of regulations establishing maximum permitted floor area, building setback requirements, maximum height and bulk, minimum open space standards, and required retail ground floor uses have been set forth. (c) For the areas in the required retail frontage area as designated by the Downtown Plan, it is intended that ground floor retail and service uses with windows be provided to maintain downtown's commercial vitality and continuity within the retail core. Uses within this area should enhance the pedestrian scale of the downtown core and allow for a compact walking environment in which all shopping opportunities are easily accessible. It is intended that all uses in this area maintain ground floor visibility to serve patrons on an unannounced or drop-in basis, conduct a majority of their business face-to-face on the premises with their customers, and maintain retail storefronts comparable to traditional retail sales operations, including display of goods and services for sale. (d) The Central Business District zoning district will be restricted to those properties within a parking assessment district. It is the intent of these regulations to insure the continued growth and development of the downtown area, thereby enabling it to remain an important retail, cultural, entertainment, business, financial, and medical center of the City and of mid-San Mateo County. Residential uses will be encouraged by increased housing densities in the downtown area in order to provide a wide range of housing opportunities for growing number of downtown employees, as well as existing residents. (e) It is the intent of these regulations to encourage development of higher intensity than in other parts of City in order to create the concentration of development and activity appropriate to a major business center. Development intensities should vary by subarea to minimize impacts on adjacent areas, moderate transportation and parking requirements, preserve essential physical characteristics of the primary shopping area, conserve architectural, historical and natural values and make new residential development possible."
    },
    {
      "heading": "27.38.020 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.38.020",
      "text": "Unless otherwise provided in this title, uses of building or land in this district and buildings hereafter erected, structurally altered or enlarged shall be limited to the following uses: (a) Any use permitted in the C2 District, except an animal hospital and emergency shelters; provided that the use limitations contained in Section 27.38.110, Required Retail Frontage, shall apply to properties located within the required retail frontage area, as shown in the Downtown Plan. (b) Multiple-family dwellings, when part of a mixed use development, subject to CBD residential development standards and affordable housing requirements as adopted by City Council resolution; however, secondary units are prohibited. (c) Name plates and signs, as classified and regulated in Title 25. (d) Temporary buildings for construction purposes for a period not to exceed the duration of such construction. (e) Accessory uses which are necessary to the above-mentioned buildings and uses; including a maximum of 15% of floor area for ancillary office uses related to retail establishments located in the ground floor area of the district, and which are not visible from the street nor located within the retail storefront area. (f) Any other use deemed similar in nature and operation that is determined by the zoning administrator to be compatible with existing and permitted uses allowable under the CBD-Central Business District zoning, and is deemed desirable in serving the downtown core area and the community at large."
    },
    {
      "heading": "27.38.030 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.38.030",
      "text": "The following uses may also be permitted if their site locations and proposed development plans are first approved as provided in Chapters 27.06 through 27.12, 27.62, 27.74, 27.78 and 27.80; however, the specific use limitations contained in Section 27.38.110, Required Retail Frontage, shall apply to properties located within the required retail frontage area, as shown in the Downtown Plan: (1) Amusement enterprises, commercial; (2) Clubs, lodges and fraternal organizations, including the serving of food and beverages to members and their guests, and including such other facilities customarily provided for the comfort and convenience of the membership; (3) Municipal or privately owned (religious or eleemosynary) recreation building or community center, including YWCA and YMCA buildings; (4) Nonresidential planned unit developments; (5) Public utility service uses and electrical substations; (6) Bus or train terminal or other public transportation facilities; (7) Fire and police stations; (8) Post office, and other government agencies; (9) Public art galleries, museums, and libraries; (10) Telephone exchange or communications building, antenna towers and other outdoor equipment essential to the operation of the exchange or communications building; (11) Auditorium, stadium, arena, armory, gymnasium, and other similar places for public events; (12) Automobile service stations only when fully enclosed within a parking structure or other building; (13) Churches and other places of religious worship except on parcels located within the required retail frontage area; (14) Convalescent homes, rest homes, and nursing homes; (15) Schools, philanthropic institutions, and day care facilities; (16) Parking facilities: (i) Parking lots outside the limited parking zone of the Central Parking and Improvement District, (ii) Parking garages, private parking garages within the parking expansion zone of the Central Parking and Improvement District, and public parking garages; (17) Hospitals and sanitariums, but not including animal hospitals; (18) Mortuaries; (19) Parks and community centers; (20) Residential planned developments, subject to CBD residential development standards and affordable housing requirements as adopted by City Council resolution; (21) Fast food restaurants, without drive-through or drive-in facilities; (22) Businesses selling or renting firearms as defined by Penal Code Section 12001(b); (23) Drive-through facilities for financial institutions and for pharmacies dispensing only prescriptions or medicinal goods at the drive-through facility. Drive-through facilities for pharmacies shall be subject to the parking requirements for financial institution drive-through uses, as enumerated in Municipal Code Section 27.64.160(7)(a)."
    },
    {
      "heading": "27.38.040 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.38.040",
      "text": "All nonresidential uses permitted in this district shall be subject to the following conditions: (a) Automobile service stations, automobile repair facilities and other similar automobile service uses are not permitted, with the exception of an automobile service station fully enclosed within a parking structure or other building. (b) There shall be no manufacturing, processing or treatment of products other than those which are clearly incidental and essential to the retail business conducted on the same premises. (c) All permitted uses in this district shall be conducted without objection from adjoining users due to odor, dust, smoke, noise, vibration, or other similar cause. (d) Any exterior sign displayed shall pertain only to a use conducted within the building. (e) All uses, including storage of equipment, materials, supplies, and commercial vehicles for off-site business permitted under this chapter shall be conducted wholly within an enclosed building, except as may be specifically authorized by special use permit or as an accessory use to an approved permitted or special use. (f) All ground floor uses shall maintain visibility of their space from the street and maintain retail storefronts comparable to traditional retail sales operations, including display of goods and services for sale."
    },
    {
      "heading": "27.38.050 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.38.050",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64. Parking requirements for residential uses may be satisfied by a contract with the CPID or payment of in-lieu fees, provided at least one (1) parking space per unit is provided on-site."
    },
    {
      "heading": "27.38.060 MAXIMUM FLOOR AREA RATIO—LOT COVERAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.38.060",
      "text": "The maximum floor area ratio and coverage shall be as follows: (a) The floor area ratio shall not exceed 3.0. (b) The maximum parcel coverage is 100%. (c) In this district, floor area devoted to above grade structured parking and lot area devoted to surface parking shall be included in the gross floor area for the purpose of calculating maximum permitted floor area ratio. (d) For the downtown block bounded by B Street, Ellsworth Avenue, First Avenue and Second Avenue, floor area exclusions may be permitted for historic preservation in accordance with Land Use Element Area Specific Policy 3(c)."
    },
    {
      "heading": "27.38.080 MAXIMUM BUILDING HEIGHT AND BULK.",
      "id": "/us/ca/cities/san-mateo/code/27.38.080",
      "text": "Structures in this zone shall not exceed the maximum height and bulk as set forth in Chapter 27.40, Building Height and Bulk Overlay District and the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.38.090 OPEN SPACE REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.38.090",
      "text": "(a) Open space shall be provided in an amount equal to one percent (1%) of the nonresidential floor area of the project, not including parking, provided that there shall be no requirement for open space where the resulting open space would be less than 200 square feet. (b) This required open space shall be usable open space located at ground level directly accessible to a public sidewalk with a minimum width along the sidewalk of 25 feet. Fifty percent of the required open space shall be unshaded between noon and 2:00 p.m. at the spring and fall equinox except where the open space is already shaded by an existing building and no other opportunities exist on the site. This open space area shall include provisions for public use facilities, such as seating for the public in the public areas."
    },
    {
      "heading": "27.38.100 BUILDING LINE AND SETBACK STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.38.100",
      "text": "In this district, building line and setbacks standards shall be as follows: (a) New developments shall be built to the property line to a minimum height of 26 feet, up to the maximum height as permitted in the street wall area or to the maximum height permitted for parcels outside the street wall area, except where a setback is required to meet ground floor open space requirements or where a setback buffer is required adjacent to a residential district pursuant to the Building Height and Bulk Plan in the Downtown Plan. (b) Up to 25% of the building line may be set back from the property line to provide for open space in excess of that required where the building is along a street designated for required retail frontage. An additional 15% may be set back in addition to the 25% if the site is not along a street designated for required retail frontage. (c) Transfers of these requirements may be permitted among properties by Planning Commission approval of a special permit where the requirements are met for the entire block face. A transfer shall be by an agreement between the property owner and the City and shall be recorded."
    },
    {
      "heading": "27.38.110 REQUIRED RETAIL FRONTAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.38.110",
      "text": "The following provisions apply in the required retail frontage area as shown in the City's Downtown Plan (the \"Required Retail Frontage\"): (a) Permitted Uses. The following uses are permitted on the ground floor subject to the requirements in Section 27.38.040, Conditions of Use, and the standards listed in subsection (c) below: (1) Retail Sales. Uses principally engaged in retail sale or rental of consumer or household goods, including ancillary repair services. These retail uses are characterized by face-to-face transactions conducted by both the buyer and seller on the business premises. Retail businesses that conduct a majority of their sales (over 50%) via the Internet or other means of telecommunications are not considered \"retail\" for the purposes of this section. (2) Personal Services. Uses principally providing services of a personal convenience nature to the individual consumer. These types of uses are primarily engaged in the provision of frequent or recurrent needed services of a personal nature. Typical personal services uses include, but are not limited to, beauty and hair salons, shoe repair shops and tailor shops. This definition of \"Personal Services\" does not include professions as defined in Section 5.24.160 of the City of San Mateo Municipal Code or any similar professions. (3) Eating and Drinking Services. Uses principally engaged in the preparation and retail sale of food and/or beverages, but excluding uses principally involving food preparation for off-site catering. (4) Theaters and Cultural Facilities. Uses providing entertainment such as motion pictures, plays or operas or cultural facilities such as a museum. (5) Banks. Uses providing financial services including banks, savings and loan institutions, lending institutions, and credit unions unless located at the intersection of two (2) streets within the required retail frontage area as shown in the Downtown Plan; banks and other financial services are prohibited at these corner locations. Such uses shall be retail service in nature, dedicated to serving the general customer, and not be open by appointment only. At least 50% of the ground floor area shall be devoted to this type of retail, customer serving use. (b) Special Uses. The following uses are permitted subject to approval of a special use permit: (1) All Properties. Any other use deemed similar in nature and operation to the permitted uses, and found to be consistent with the purposes of this chapter and the policies of the Downtown Plan, may be authorized upon approval of a special use permit by the Planning Commission, subject to the provisions of Chapters 27.08, Rules of Procedure, and 27.74, Special Use Permits, unless appealed to the City Council in accordance with Section 27.08.060. (2) Ground Floor Dependent Offices on Non-Corner Properties. Offices used for on-site property management, or for professional or consulting services, including, but not limited to, travel agencies, insurance agencies, income tax preparers, real estate agencies and notary publics, when not exceeding 2,500 square feet per building and not located at the intersection of two (2) streets within the required retail frontage area as shown in the Downtown Plan. Such uses shall require ground floor visibility to serve patrons on an unannounced or drop-in basis, shall conduct a majority of their business face-to-face on the premises with their customers, and shall maintain retail storefronts comparable to traditional retail sales operations, including display of goods and services for sale. (c) Standards. (1) Ground Floor Retail Frontage Width and Depth Standards. (i) For non-corner properties with street frontage widths of 25 linear feet or less, at least 67% of the building's street frontage, to a depth of 60 feet, shall be limited to the permitted uses specified above. (ii) For non-corner properties with street frontage widths greater than 25 linear feet, at least 75% of the building's street frontage, to a depth of 60 feet, shall be limited to the permitted uses specified above. (iii) Reduction in Ground Floor Retail Frontage Width and Depth Requirement. Reductions in the above requirements may be authorized upon approval of a special use permit by the Planning Commission, subject to the provisions of Chapters 27.08, Rules of Procedure, and 27.74, Special Use Permits, and if each of the following findings can be made in addition to the findings required for special use permits: (A) The property has physical limitations such as narrow building or lot width, or an unusual building or lot configuration which renders it infeasible to meet the retail depth and width requirements set forth above; and (B) The proposed uses and associated changes to the building and property are consistent with the purposes of this chapter, and applicable policies pertaining to downtown including, but not limited to the General Plan, Downtown Plan, and Pedestrian Master Plan. (2) Public Access. All permitted and specially-permitted uses shall be directly accessible from a public sidewalk or a plaza accessible from the public sidewalk along the required frontage. (3) View of Interior Space. New or reconstructed building walls at the ground level shall have at least 75% of the width along the street devoted to pedestrian entrances, transparent show or display windows of at least two (2) feet in depth, or windows affording a view of retail, office, or lobby space. (4) Ground Floor Entries to Other Uses. (i) For lots with street frontage widths of 25 linear feet or less, not more than 33% of the street frontage shall be devoted to entrances to uses other than the above permitted uses. (ii) For lots with street frontage widths greater than 25 linear feet, not more than 25% of the street frontage shall be devoted to entrances to uses other than the above permitted uses. (5) Location of Parking. Surface parking shall not be permitted within 50 feet of property lines designated for required retail frontage and shall be required to be located behind a building meeting the requirements of this title. (6) Second Floor Offices. Second floor offices, including medical and dental clinics, and financial institutions are permitted only if the ground floor of the structure is occupied by one (1) of the permitted uses listed above."
    },
    {
      "heading": "27.38.120 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.38.120",
      "text": "(a) When a CBD-zoned plot abuts any residential district, an adequate landscape planting buffer shall be maintained adjacent to the R-zoned property. The depth of this buffer along interior lot lines shall be equal to at least one-half the height of the building, or 15 feet, whichever is greater. No buffer shall be required along street frontages abutting R-zoned property. Open parking otherwise in conformance with standards listed in this chapter may be permitted within the required buffer area except as required in Section 27.64.140 of the off-street parking code. No portion of the building is exempt from the buffer requirements. (b) Required Fences or Walls. A solid fence or solid wall is required for parcels abutting residential districts as provided in Section 27.84.030."
    },
    {
      "heading": "27.38.130 RESIDENTIAL DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.38.130",
      "text": "In this district, residential uses shall be permitted as part of mixed use developments, subject to the following conditions: (a) Unit Density. (1) CBD (Central Business District). Residential development on properties zoned CBD shall not exceed 50 units per acre regardless of parcel size. (2) CBD/R (Central Business District/Residential Overlay District—Mixed Use). Residential development on properties zoned CBD/R shall be subject to /R density standards. (b) Floor Area. Any portion of lot area used for surface parking or above grade parking shall be included in floor area for the purposes of computing maximum permissible floor area. (c) Open Space. Residential development shall include private usable open space equal to at least 80 square feet per dwelling unit or common usable open space equal to at least 150% of the private usable open space requirements, or a combination of both. Private usable open space used to fulfill this requirement shall have a usable area of not less than 75 square feet and shall not be less than six (6) feet in any dimension."
    },
    {
      "heading": "27.38.140 DOWNTOWN ECONOMIC DEVELOPMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.38.140",
      "text": "To encourage development of large, vacant, underutilized parcels as designated in the Downtown Plan, exceptions from land use standards contained in this title may be granted upon approval of a downtown economic development permit by the City Council for properties in the Central Business District (CBD). Approval of such an application shall be based on the following findings: (a) The project is consistent with the goal statements of the Downtown Plan; (b) The project is of an excellent design quality and is consistent with the Downtown Retail Core and Downtown Historic District Design Guidelines; (c) The project is a significant development which presents a substantial economic development opportunity for the City and attempts to maximize use of the site; (d) The project has a minimum building floor area ratio of 1.0 (not including surface and structured parking) or includes a substantial public improvement such as a public parking garage, open space plaza, public marketplace or other public facility; and (e) Any unmitigated significant impacts are outweighed by the project's economic, social or other benefits. In no case, however, shall the project exceed the maximum height and bulk standard and building intensity standard as set forth in Chapter 27.40, Building Height and Bulk Overlay District and the Building Height and Intensity Plan of the General Plan."
    }
  ],
  "Chapter 27.39 CBD SUPPORT DISTRICT—CENTRAL BUSINESS DISTRICT SUPPORT": [
    {
      "heading": "27.39.010 PURPOSE—INTENT.",
      "id": "/us/ca/cities/san-mateo/code/27.39.010",
      "text": "The purpose of the CBD Support District is to encourage commercial uses which both support traditional downtown (CBD) uses as well as serve adjacent residential neighborhoods. It is intended that the commercial uses in this area will serve as a link between the Gateway and CBD. Residential uses will also be encouraged in order to provide housing opportunities for downtown employees, as well as existing and future residents."
    },
    {
      "heading": "27.39.020 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.39.020",
      "text": "Unless otherwise provided in this title, uses of buildings or land in this district and buildings hereafter erected, structurally altered or enlarged shall be limited to the following uses: (1) Any use permitted in the CBD District."
    },
    {
      "heading": "27.39.030 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.39.030",
      "text": "The following uses may also be permitted if their site locations and proposed development plans are first approved as provided in chapters 27.06 through 27.12, 27.62, 27.72, 27.78 and 27.80: (1) Any of the special uses in the CBD District, in addition to: (a) Automobile service stations. (b) Fast food restaurants, including drive-through and drive-in service, subject to the following design criteria in addition to the standards required under this chapter: (i) New construction should incorporate dominant architectural elements, colors and materials common to nearby buildings. (ii) The building's street facade shall provide visual interest through the use of transparent windows or architectural detailing. (iii) Pedestrian access shall be encouraged through the use of recessed doors and windows, awnings, street trees and sidewalk furniture. (iv) Landscaping shall be used to screen drive-through or drive-in aisles from the public right of way and shall be used to minimize the visual impact of readerboard signs and directional signs. (v) The driveway shall be designed to minimize conflicts between pedestrians and vehicles, and shall provide adequate site visibility. (vi) A litter control plan shall be submitted with an application. The litter control plan shall indicate the location of trash receptacles and provisions for employee maintenance of the site."
    },
    {
      "heading": "27.39.040 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.39.040",
      "text": "All non-residential uses permitted in this chapter shall be subject to the following conditions: (a) There shall be no manufacturing, processing or treatment of products other than those which are clearly incidental and essential to the retail business conducted on the same premises. (b) All permitted uses in this district shall be conducted without objection from adjoining users due to odor, dust, smoke, noise, vibration, or other similar cause. (c) Any exterior sign displayed shall pertain only to a use conducted within the building. (d) All uses, including storage of equipment, materials, supplies and commercial vehicles for off-site business permitted under this chapter shall be conducted wholly within an enclosed building, except as may be specifically authorized by special permit or an accessory use to an approved permitted or special use."
    },
    {
      "heading": "27.39.050 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.39.050",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64."
    },
    {
      "heading": "27.39.060 MAXIMUM FLOOR AREA RATIO—LOT COVERAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.39.060",
      "text": "Maximum floor area ratio and lot coverage shall be required and calculated as in Section 27.38.060."
    },
    {
      "heading": "27.39.070 MAXIMUM BUILDING HEIGHT AND BULK.",
      "id": "/us/ca/cities/san-mateo/code/27.39.070",
      "text": "Structures in this zoning district shall not exceed the maximum height and bulk as set forth in Chapter 27.40 Building Height and Bulk Overlay District and the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.39.080 OPEN SPACE REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.39.080",
      "text": "Open space shall be provided as designated in Section 27.38.090."
    },
    {
      "heading": "27.39.090 BUILDING LINE AND SETBACK STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.39.090",
      "text": "Building line and setback standards shall be as designated in Section 27.38.100 except as follows: (1) A setback of up to ten (10) feet for landscaping may be provided within front or street side yards. New development shall be built to the property line where a structure on an abutting property, on the same side of the street, is built to the front or street side property lines. (2) On streets not designated as Required Retail Frontage, a building may be set back from the street to accommodate the following uses: a. automobile service stations, subject to the standards contained in Chapter 27.77; b. fast food restaurants with drive-through facilities, subject to the standards contained in Section 27.39.030."
    },
    {
      "heading": "27.39.100 REQUIRED RETAIL FRONTAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.39.100",
      "text": "Within the Required Retail Frontage area as shown on the Downtown Specific Plan land use map, the requirements of Section 27.38.110 shall apply, except as follows: (a) Surface parking shall not be permitted within fifty (50) feet of property lines designed for Required Retail Frontage and shall be required to be located behind a building meeting the requirements of this title, except when the following conditions are met: (1) A building of at least 8,000 square feet exists on site and the parking will be located between the building and property line: (2) The surface parking is being provided to fulfill requirements for uses within the existing building; (3) The area to be paved for surface parking is unimproved; and (4) At least 6 feet and up to a maximum of 10 feet of landscaping is installed between the property line and the surface parking lot for screening. (b) Temporary (a maximum of 5 years) surface parking in a City or City agency owned parking lot shall be permitted. A minimum of six feet of landscaping shall be installed between the property line and any surface parking."
    },
    {
      "heading": "27.39.110 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.39.110",
      "text": "Where a CBD Support zoned plot abuts any residential district, buffers as required in Section 27.38.120 shall be provided."
    },
    {
      "heading": "27.39.120 RESIDENTIAL DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.39.120",
      "text": "In this district, residential uses shall be permitted as part of mixed-use developments, subject to the City's Objective Design Standards as adopted by resolution of the City Council and requirements of Section 27.38.130."
    }
  ],
  "Chapter 27.40 BUILDING HEIGHT AND BULK": [
    {
      "heading": "27.40.010 SCOPE.",
      "id": "/us/ca/cities/san-mateo/code/27.40.010",
      "text": "This chapter applies only to the study area encompassed by the Downtown Specific Plan of the General Plan of the City as adopted by the City Council and as may be amended by the Council from time to time. No special permit is required for buildings or structures which meet the height and bulk standards of this chapter."
    },
    {
      "heading": "27.40.020 HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.40.020",
      "text": "Structures and building heights as defined in Section 27.04.080 shall be permitted to be developed provided they do not exceed the maximum height delineated for the respective project sites as shown on the Building Height and Bulk Plan in the Downtown Specific Plan. High-rise buildings over fifty-five (55) feet in height may be permitted if a site plan and architectural review is first approved by the Planning Commission as provided in Chapter 27.06."
    },
    {
      "heading": "27.40.030 BULK.",
      "id": "/us/ca/cities/san-mateo/code/27.40.030",
      "text": "(1) Structures and buildings shall be developed in accordance with the following standards: (2) Bulk is measured as illustrated in the following diagrams:  (3) Variations to the maximum building bulk for buildings greater than fifty-five (55) feet in height may be permitted by a special use permit approved by the Planning Commission subject to the following criteria: (A) A better and more appropriate design for the site is achieved than without the variation; (B) The parcel coverage will not exceed 40%; (C) The parcel size is at least one and one half (1.5) acres; (D) The design preserves view corridors and sunlight access as well as a design that conforms to all requirements of the Downtown Specific Plan; (E) The design conforms to the goals, policies and the streetwall area standards of the Downtown Specific Plan; (F) The project site is designated for residential use in the Downtown Specific Plan, and the floor area above fifty-five (55) feet is utilized exclusively for residential use."
    }
  ],
  "Chapter 27.42 STREET WALL AREA DISTRICT": [
    {
      "heading": "27.42.010 STREET WALL AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.42.010",
      "text": "Structures and buildings on parcels identified as Street Wall Area on the Building Height and Bulk Plan in the Downtown Specific Plan shall be developed in accordance with the following diagram:  (1) The maximum building height at the parcel boundary is equal to the horizontal distance between midpoint of the public right-of-way and the parcel boundary (A) or thirty-six (36) ft., whichever is greater. (2) The maximum depth of the street wall area is equal to two times the distance of (A). (3) The building height at any point within the street wall area shall not exceed the slope defined by a forty-five degree (45) angle measured from the midpoint of the public right-of-way, except as allowed by section (1) above at the parcel boundary. (4) The maximum building height beyond the street wall area shall be controlled by the Building Height and Bulk Plan in the Downtown Specific Plan. (5) The area above the street wall area as defined in Section (3), shall be open to the sky. Elevators, stairwells and other mechanical or other appurtenances are not permitted to protrude above the street wall area. Allowable intrusions above the street wall area are limited to minor architectural detailing not exceeding four (4) feet in height and parapets including railings and arbors and landscaped planting areas, subject to approval of a site plan and architectural review. (6) Outdoor uses shall be allowed in area (B)."
    }
  ],
  "Chapter 27.44 E1 DISTRICTS—EXECUTIVE PARK": [
    {
      "heading": "27.44.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.44.010",
      "text": "The E1 district is intended to provide, create, preserve, and enhance areas devoted primarily to conference, research, and administrative activities in attractive surroundings. Accessory uses include personal services, restaurants, health clubs, day care, and limited retail sales. E1 zoning is typically appropriate to large acreages with good accessibility which can be suitably landscaped and made compatible with adjacent residential development."
    },
    {
      "heading": "27.44.020 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.44.020",
      "text": "The following uses shall be permitted: (a) Administrative, executive, and professional offices, provided that the professional offices are limited to those professions listed in Section 5.24.160, and including similar professional occupations, and provided that no office of a veterinarian shall include an animal hospital or kennel. (b) Accessory uses; including, but not limited to: (1) Sale of personal goods and services, when provided in the principal building, including, but not limited to, the following: (A) Flower, food, and news vending; (B) Printing and photocopying; (C) Travel agencies; (D) Ticket outlets; (2) Other services which are customary appurtenant uses. (c) Health and recreation facilities. (d) Public utility and service uses. (e) Financial and business offices and related facilities. (f) Research laboratories (experimental and testing), provided no production or manufacturing occurs, and provided that all activities conform with the performance standards established for the M1 district. (g) Residential units, only on parcels designated with a residential overlay district classification subject to R3 district \"Minimum Development Standards\" in Section 27.22.040 and affordable housing requirements as adopted by City Council resolution, unless otherwise specified in Chapter 27.29; however, secondary units are prohibited. (h) Restaurants without drive-through facilities. (i) Schools and day care facilities. (j) Warehousing, storage, and distribution facilities as accessory uses but not exceeding 10,000 square feet per establishment or not more than 60% of gross floor area per establishment. (k) Other compatible uses as determined by the Zoning Administrator."
    },
    {
      "heading": "27.44.030 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.44.030",
      "text": "The following uses may also be permitted subject to approval of a special use permit: (a) Alternative financial services, subject to the restrictions set forth in Section 27.30.020; (b) Automobile gasoline service station; (c) Clubs, lodges, and fraternal organizations; (d) Hotels; (e) Parking facilities, as a principle use; (f) Religious institutions; (g) Residential units on parcels without a residential overlay district classification subject to R3 District \"Minimum Development Standards\" in Section 27.22.040 and affordable housing requirements as adopted by City Council resolution, unless otherwise specified in Chapter 27.29; however, secondary units are prohibited; and (h) Other compatible uses as determined by the Zoning Administrator subject to the granting of a special use permit."
    },
    {
      "heading": "27.44.040 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.44.040",
      "text": "Permitted uses and special uses in the E1 districts are subject to the following conditions: (a) All public utility service connections to structures and facilities shall be located underground in accordance with specifications to be approved by the Director of Public Works and in accordance with the rules and regulations applicable thereto as approved by the Public Utilities Commission of the State; (b) All uses permitted within this district shall be conducted within completely enclosed buildings and shall be subject to the same \"performance standards\" set forth in Chapter 27.56, except as may be specifically authorized by special permit."
    },
    {
      "heading": "27.44.050 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.44.050",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64."
    },
    {
      "heading": "27.44.060 FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.44.060",
      "text": "The maximum floor area ratio of buildings and structures on a zoning plot shall be as follows: (a) In an E1-.4 district, the floor area ratio shall not exceed .4; (b) In an E1-.5 district, the floor area ratio shall not exceed .5; (c) In an E1-.62 district, the floor area ratio shall not exceed .62; (d) In an E1-1 district, the floor area ratio shall not exceed 1.0; (e) In an E1-2 district, the floor area ratio shall not exceed 2.0."
    },
    {
      "heading": "27.44.065 PARCEL COVERAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.44.065",
      "text": "A minimum of 35% at-grade open space shall be provided on the parcel. Open space shall contain landscaping and/or decorative outdoor landscape elements, water features, paved or decorated surfaces of rock, stone, brick or other similar material (excluding driveways, parking, loading, or storage areas), and sculptural elements. "
    },
    {
      "heading": "27.44.070 MINIMUM PLOT AREA STANDARDS AND DIMENSIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.44.070",
      "text": "All buildings and structures hereafter erected in the E1 district, shall be on a zoning plot having an area of not less than 20,000 square feet, and a minimum width at the building line of not less than 100 feet."
    },
    {
      "heading": "27.44.075 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.44.075",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.44.080 MINIMUM YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.44.080",
      "text": "No building or open parking areas shall be constructed or enlarged unless the following yards are provided and maintained in connection with such buildings, structures, parking lots, or enlargements: yards not less than 15 feet along any street frontage."
    },
    {
      "heading": "27.44.090 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.44.090",
      "text": "(a) When an E1-zoned plot is contiguous to any residential district, an adequate landscape buffer shall be maintained adjacent to the R-zoned property. The depth of this buffer along street frontages shall be at least equal to one-half the height of the building measured from the property line. The depth of this buffer along interior lot lines shall be at least equal to one-half the height of the building, or 15 feet, whichever is greater. Open parking otherwise in conformance with standards listed in this chapter may be permitted within the required buffer area except in the last 15 feet. (b) Required Fences or Walls. A solid fence or solid wall is required for parcels abutting residential districts as provided in Section 27.84.030."
    }
  ],
  "Chapter 27.48 E2 DISTRICTS—EXECUTIVE OFFICES": [
    {
      "heading": "27.48.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.48.010",
      "text": "The E2 District is intended to create and maintain professional and administrative offices. Allowed uses are the same as in the E1 District. The E2 District is intended for small sites served by nearby commercial facilities."
    },
    {
      "heading": "27.48.020 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.48.020",
      "text": "The following uses are permitted: (a) Permitted uses in the E1 district; (b) Residential units, only on parcels designated with a residential overlay district classification subject to R4 district \"Minimum Development Standards\" in Chapter 27.24 and affordable housing requirements as adopted by City Council resolution, except as otherwise specified in Chapter 27.29; however secondary units are prohibited."
    },
    {
      "heading": "27.48.030 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.48.030",
      "text": "Special Uses in the E1 district may also be allowed subject to approval of a special use permit. Residential units on parcels without a residential overlay district classification subject to R4 district \"Minimum Development Standards\" in Section 27.24.040 and affordable housing requirements as adopted by City Council resolution, unless otherwise specified in Chapter 27.29; however, secondary units are prohibited."
    },
    {
      "heading": "27.48.040 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.48.040",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64."
    },
    {
      "heading": "27.48.050 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.48.050",
      "text": "Permitted uses and special uses in the E2 districts are subject to the following condition: All uses permitted within this district shall be conducted within completely enclosed buildings and shall be subject to the same \"performance standards\" set forth in Chapter 27.56, except as may be specifically authorized by special permit."
    },
    {
      "heading": "27.48.060 FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.48.060",
      "text": "The maximum floor area ratio for buildings and structures on a zoning plot shall be as follows: (a) In an E2-.5 district, the floor area ratio shall not exceed 0.5; (b) In an E2-1 district, the floor area ratio shall not exceed 1.0; (c) In an E2-1.5 district, the floor area ratio shall not exceed 1.5; (d) In an E2-2 district, the floor area ratio shall not exceed 2.0."
    },
    {
      "heading": "27.48.065 PARCEL COVERAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.48.065",
      "text": "A minimum of 20 percent at-grade open space shall be provided on the parcel, except in the /R overlay district where 10 percent minimum at-grade open space is required. Open space shall contain landscaping and/or decorative outdoor landscape elements, water features, paved or decorated surfaces of rock, stone, brick or other similar material (excluding driveways, parking, loading, or storage areas), and sculptural elements. "
    },
    {
      "heading": "27.48.070 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.48.070",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.48.080 MINIMUM PLOT AREA STANDARDS AND DIMENSIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.48.080",
      "text": "All buildings and structures hereafter erected in the E2 District shall be on a zoning plot having an area of not less than six thousand square feet and a width of not less than fifty feet at the building line."
    },
    {
      "heading": "27.48.090 MINIMUM YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.48.090",
      "text": "No buildings or open parking areas shall be constructed or enlarged unless the following yards are provided and maintained in connection with such buildings, structures, parking lots, or enlargements: yards not less than seven and one-half feet along any street frontage."
    },
    {
      "heading": "27.48.100 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.48.100",
      "text": "When an E2 zoned plot is contiguous to any residential district, an adequate landscape buffer shall be maintained adjacent to the R zoned property. The depth of this buffer along street frontages shall be at least equal to one-half the height of the building measured from the property line. The depth of this buffer along interior lot lines shall be at least equal to one-half the height of the building, or fifteen feet, whichever is greater. Open parking otherwise in conformance with standards listed in this chapter may be permitted within the required buffer area except in the last six feet."
    }
  ],
  "Chapter 27.54 MANUFACTURING DISTRICTS": [
    {
      "heading": "27.54.010 USE AND BULK REGULATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.54.010",
      "text": "Use and bulk regulations applying specifically to manufacturing districts are set forth in Chapter 27.56. Also applying to manufacturing districts are additional regulations set forth in other chapters of this title as follows: (1) Chapters 27.02, 27.16, 27.66, 27.68, 27.70 and 27.82, General Provisions; (2) Chapter 27.04, Definitions; (3) Chapter 27.72, Nonconforming Buildings and Uses; (4) Chapter 27.64, Off-street Parking and Loading; (5) Chapters 27.06 through 27.12, 27.62, 27.74, 27.78 and 27.80, Administration."
    }
  ],
  "Chapter 27.56 M1 DISTRICTS—MANUFACTURING": [
    {
      "heading": "27.56.005 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.56.005",
      "text": "The Manufacturing District is intended to create and maintain light manufacturing, warehousing, and distribution facilities where air emissions, noise generation, and hazardous materials handling are limited."
    },
    {
      "heading": "27.56.010 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.56.010",
      "text": "The following uses are permitted: (a) Permitted uses in commercial districts, except residential uses which are not permitted; (b) Assembly, production, processing, cleaning, testing, or repair of products; (c) Contractor or construction shops; (d) Laboratories; medical, dental, research, experimental, and testing; (e) Residential dwelling units for security personnel when located on the premises where they are employed; (f) Wholesale and warehousing; excluding storage of inflammable liquids; (g) Accessory uses to principle uses; and (h) Other compatible uses as determined by the zoning administrator."
    },
    {
      "heading": "27.56.020 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.56.020",
      "text": "The following uses may also be permitted subject to approval of a special use permit: (a) Special uses allowed in commercial districts except that residential uses and secondary units are not permitted; (b) Storage of impounded motor vehicles on an open lot; (c) Theaters, drive-in; (d) Wholesale storage of inflammable liquids; and (e) Other compatible uses as determined by the zoning administrator subject to the approval of a special use permit."
    },
    {
      "heading": "27.56.030 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.56.030",
      "text": "In the M1 districts, the permitted uses in this chapter are subject to the following: (a) Any assembly production, processing, cleaning, servicing, testing, repair or storage of goods, materials, or products shall conform with the performance standards set forth in this chapter. (b) All business, production, servicing and processing uses, including storage, equipment, materials, supplies and commercial vehicles for off-site businesses shall take place within completely enclosed buildings, except as may be otherwise specifically authorized. Open off-street loading facilities and open off-street parking facilities for the storage of motor vehicles may be unenclosed throughout the district except for such screening of parking and loading facilities as may be required under the provisions of Chapter 27.64. (c) All parked and impounded motor vehicles in an open lot shall have such lot completely enclosed by a solid wall or fence, including doors or gates thereto, not less than six feet in height. All such motor vehicles shall be parked or placed in an orderly manner within such fenced lot with clear and adequate passageways to allow free and unobstructed access and movement of the fire department in case of fire. The manner of handling and keeping impounded motor vehicles shall, at all times, be subject to the approval of the chiefs of the police and fire departments. (d) Such conditions relating to noise emissions, lighting and hours of operation that are reasonably necessary in the interests of the public health, welfare and safety. (e) When granting a special permit for the storage of impounded motor vehicles, the Planning Commission shall specify the expiration date of said permit and the conditions to be met for its renewal, and may specify periodic reviews thereof."
    },
    {
      "heading": "27.56.040 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.56.040",
      "text": "Automobile parking and loading facilities shall be provided as required, or permitted, in Chapter 27.64."
    },
    {
      "heading": "27.56.050 MAXIMUM FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.56.050",
      "text": "Maximum floor area ratio of buildings and structures on a zoning plot shall not exceed 1.0."
    },
    {
      "heading": "27.56.055 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.56.055",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.56.060 MINIMUM FRONT YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.56.060",
      "text": "A front yard of not less than fifteen feet in depth shall be provided. However, where lots within the same block and comprising forty percent of the frontage on the same street are already developed on the effective date of this code with front yards with an average depth of less than fifteen feet, then such average depth shall be the required front yard depth for such frontage in said block."
    },
    {
      "heading": "27.56.070 MINIMUM SIDE YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.56.070",
      "text": "A side yard shall be provided along each side lot line. Each side yard shall be not less in width than ten percent of the lot width but need not exceed ten feet in width."
    },
    {
      "heading": "27.56.075 BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.56.075",
      "text": "Buffers shall be provided in accordance with the following regulations: (1) Parcels fronting on a street with at least eighty (80) percent of the frontage directly across the street between two (2) consecutive intersecting streets in a residential district, shall provide a front yard pursuant to the front yard requirements of the residential district; (2) Side parcel lines coinciding with a side or rear parcel line of a property in a residential district shall provide a side yard equal to the minimum required side yard in the residential district; (3) Rear parcel lines coinciding with a side parcel line of a parcel in a residential district shall provide a rear yard equal in dimension to the minimum required side yard in the residential district; (4) Rear parcel lines coinciding with a rear parcel line of a property in a residential district shall provide a rear yard not less than ten (10) feet in depth; (5) Extensions of front or side parcel lines coinciding with the front parcel line of a property in a residential district, shall provide a yard equal in depth to the minimum required front yard of the residential district for a distance of at least twenty-five (25) feet, including the width of any intervening alley from such the residential parcel line; (6) Required yards shall be unobstructed from the ground level to the sky; (7) Fast-food establishments shall be separated from each other and from residential districts by no less than one hundred (100) feet measured from the nearest parcel lines. However, multiple fast-food establishments may be closer than one hundred (100) feet in a shopping center; (8) Districts adjacent to an open space district shall provide at least a fifteen (15) foot yard. (9) Required fences or walls. A solid fence or solid wall is required for parcels abutting residential districts as provided in Section 27.84.030 of this title."
    },
    {
      "heading": "27.56.080 PERFORMANCE STANDARDS GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.56.080",
      "text": "Any use established hereafter in an M1 district, shall be so operated as to comply with the performance standards set forth as follows in Section 27.56.090 through 27.56.150."
    },
    {
      "heading": "27.56.090 NOISE.",
      "id": "/us/ca/cities/san-mateo/code/27.56.090",
      "text": "Sound levels shall be measured with a sound level meter and associated octave band filter manufactured according to standards prescribed by the American Standards Association, Inc., New York, N.Y. Measurements shall be made using the flat network of the sound level meter. Impulsive type noises shall be subject to the performance standards hereinafter prescribed provided that such noises shall be capable of being accurately measured with such equipment. Noises capable of being measured, for the purpose of this title, shall be those noises which cause rapid fluctuation of the needle of the sound level meter with a variation of no more than plus or minus two decibels. Noises incapable of being so measured, such as those of an irregular and intermittent nature, shall be controlled so as not to become a nuisance to adjacent uses. At no point either on the boundary of a residence district or a commercial district or at one hundred twenty-five feet from the nearest property line of a plant or operation, whichever distance is greater, shall the sound pressure level of an individual operation or plant (other than the operation of motor vehicles and other transportation facilities) exceed the decibel levels at the designated octave bands shown hereafter for the districts indicated."
    },
    {
      "heading": "27.56.100 SMOKE—PARTICULATE MATTER.",
      "id": "/us/ca/cities/san-mateo/code/27.56.100",
      "text": "(a) No stack shall emit more than ten smoke units during any one hour, nor shall smoke of a density in excess of Ringelmann No. 2 be emitted. For the purposes of grading density of emissions, the Ringelmann chart published and used by the United States Bureau of Mines shall be employed. (b) The rate of emission of particulate matter from all sources within the boundaries of any lot shall not exceed a net figure of one pound per acre of lot area and during any one hour, computed in accordance with the procedures set forth in Chapter 27.76. (c) Dust and other forms of air pollution borne by the wind from such sources as storage areas, yards, roads, and so forth within lot boundaries shall be kept to a minimum by appropriate landscaping, paving, oiling or other acceptable means. The emission of particulate matter from such sources shall conform with the requirements of (b) above."
    },
    {
      "heading": "27.56.110 ODOROUS MATTER.",
      "id": "/us/ca/cities/san-mateo/code/27.56.110",
      "text": "The emission of odorous gases or other odorous matter from any property in such concentrations as to be readily detectable at any point along the boundaries of said property or in such concentrations as to create a public nuisance or hazard beyond such boundaries is prohibited. Any process which may involve the creation or emission of any odors shall be provided with a secondary safeguard system, so that control will be maintained if the primary safeguard system should fail. There is established as a guide in determining such quantities of offensive odors, Table III, \"Odor Thresholds,\" in Chapter 5, \"Air Pollution Abatement Manual,\" by Manufacturing Chemists Association, Inc., Washington, D.C."
    },
    {
      "heading": "27.56.120 VIBRATION.",
      "id": "/us/ca/cities/san-mateo/code/27.56.120",
      "text": "Any process or equipment which produces disturbing, earth shaking vibrations shall be set back at least three hundred feet from the property boundaries on all sides. However, in no case shall such vibrations be allowed to create a public nuisance or hazard beyond the property boundaries."
    },
    {
      "heading": "27.56.130 TOXIC OR NOXIOUS MATTER.",
      "id": "/us/ca/cities/san-mateo/code/27.56.130",
      "text": "No use on any property shall discharge across the boundaries of said property toxic or noxious matter in such concentrations as to be detrimental to or endanger the public health, safety, comfort or welfare, or cause injury or damage to other property or business."
    },
    {
      "heading": "27.56.140 GLARE—HEAT.",
      "id": "/us/ca/cities/san-mateo/code/27.56.140",
      "text": "Any operation producing intense glare or heat shall be performed within a completely enclosed building and effectively screened in such a manner as not to create a public nuisance or hazard along property boundaries."
    },
    {
      "heading": "27.56.150 FIRE AND EXPLOSIVE HAZARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.56.150",
      "text": "Fire and explosive hazards shall be subject to the fire prevention regulations in Chapter 23.28."
    }
  ],
  "Chapter 27.59 S DISTRICTS—SHORELINE DISTRICT": [
    {
      "heading": "27.59.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.59.010",
      "text": "The shoreline district (S) is established to assure that users in the proximity of the San Francisco Bay are appropriate in their relationship to the Bay ecological system, compatible with their general surroundings, and consistent with the state grant of lands to San Mateo."
    },
    {
      "heading": "27.59.020 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.59.020",
      "text": "The following uses are permitted: (1) Public parks and recreation facilities, including but not limited to public open space, parks, bathing beaches, fishing piers, marinas, boardwalks, bicycle and pedestrian paths, trails, picnic areas, and other similar uses; (2) Open space for the preservation, maintenance, and enhancement of lands in their natural state, or their restoration, and as habitat for wildlife; (3) Private boat facilities in Marina Lagoon in accordance with the following: (a) Conformance with the approved United States Army Corps of Engineers Regional Permit for the use and operation of Marina Lagoon; and (b) Development of other than single family or duplex homes, in multiple residential dwelling unit districts, commercial districts, or business districts shall provide public access and public boat ties."
    },
    {
      "heading": "27.59.030 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.59.030",
      "text": "The following uses may also be permitted if their site locations and proposed development plans are first approved as provided in Chapters 27.06 through 27.12, 27.62, 27.74 and 27.80: (a) Hotels; (b) Boatworks and related activities; (c) Restaurants; (d) Specialty retail shops in association with water-related uses; (e) Radio and television transmission towers; (f) Private recreation facilities; (g) Public harbors, including construction and maintenance of wharves, docks, piers and other structures or utilities necessary for the promotion or accommodation of water-related commerce, navigation and fisheries; (h) Public facilities, including but not limited to, transmission lines, sanitary and storm sewer installations, treatment plants, and pumping stations, streets, and water distribution systems; (i) The following uses, on properties designated as Regional/Community Commercial on the General Plan Land Use Map: (1) Mini-warehouse facilities; (2) Light industrial uses, as determined by the Zoning Administrator; (3) Ancillary office uses in conjunction with the uses allowed in this chapter. (j) Such other uses, including specific uses designated in the Shoreline Park Plan of the City, which are demonstrated to be both consistent and compatible with the Bay environment and the general area in which the uses are proposed, taking into consideration, where appropriate, a site which is particularly suited for a use by virtue of its location."
    },
    {
      "heading": "27.59.040 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.59.040",
      "text": "All uses in the S district are subject to the following conditions: (1) All uses shall be subject to the performance standards as set forth in Chapter 27.76; (2) All uses on parcels abutting water, San Francisco Bay, Marina Lagoon, San Mateo Creek, or Sixteenth Avenue Channel shall provide for public access to and along all waterways; (3) All uses on parcels abutting water may be required to make improvements along the water's edge; (4) All uses shall be consistent with the adopted shoreline plan; (5) All uses adjacent to water shall not adversely affect the water quality, should enhance the value of the water, and should protect the marine and wildlife habitat and marsh areas."
    },
    {
      "heading": "27.59.050 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.59.050",
      "text": "Automobile parking and loading facilities shall be provided as required or permitted in Chapter 27.64."
    },
    {
      "heading": "27.59.060 SETBACKS—BUFFERS.",
      "id": "/us/ca/cities/san-mateo/code/27.59.060",
      "text": "(a) When an S zoned parcel is contiguous to any R district, an adequate landscape buffer shall be maintained adjacent to the R zoned property. The depth (width) of this buffer shall be at least fifteen feet, and shall be landscaped. Parking may be located in the buffer setback area, subject to landscaping screening requirements. (b) Other setback or buffer requirements may be imposed as part of the special use procedure."
    },
    {
      "heading": "27.59.070 BUILDING HEIGHT.",
      "id": "/us/ca/cities/san-mateo/code/27.59.070",
      "text": "Building height shall not exceed the standards set forth on the Building Height Plan of the General Plan."
    },
    {
      "heading": "27.59.080 FLOOR AREA RATIO.",
      "id": "/us/ca/cities/san-mateo/code/27.59.080",
      "text": "The maximum floor area ratio for buildings and structures shall not exceed 1.0."
    }
  ],
  "Chapter 27.60 SPECIAL DISTRICTS": [
    {
      "heading": "27.60.030 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.60.030",
      "text": "Permitted uses shall be as follows: (a) All uses commonly classed as agriculture, horticulture or forestry, including crop and tree farming, and nursery operation. (b) Horse racetracks and related uses, including, but not limited to, veterinary facilities, feed storage facilities, stables, offices, restaurants, sleeping quarters, plant nurseries and equipment storage facilities. (c) One-family detached dwelling and accessory buildings provided the property (or zoning plot) upon which the dwelling is located has as its principal use one of the agricultural uses permitted above. (d) Parks, forest preserves and recreational areas, when publicly owned and operated. (e) Golf courses, regulation size, but not including \"par 3\" golf courses, commercially operated driving ranges or miniature golf courses; and provided, that no clubhouse or accessory building shall be located nearer than five feet to any dwelling. (f) Signs, advertising the sale or rental of the property upon which the sign is located. (g) Public utility facilities."
    },
    {
      "heading": "27.60.040 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.60.040",
      "text": "The following uses may also be permitted if their site locations and proposed development plans are first approved, as provided for in Chapters 27.06 through 27.12, 27.62, 27.74, 27.78 and 27.80: (a) Mining, dredging, loading, and hauling of sand, shells, salt, dirt, gravel or other aggregate, but not including equipment, buildings or structures for screening, refining, crushing, mixing, washing or storage. (b) Railroad Rights-of-Way and Trackage. Airports or aircraft landing fields. Radio and television towers, commercial. (c) Filling of lowland with noncombustible material free from refuse and food wastes. (d) Sanitary land fill, when operated or supervised by the City. (e) Kennels, commercial, and animal hospitals. (f) Public service uses: (1) Filtration plant, pumping station, and water reservoir; (2) Sewage treatment plant; (3) Other governmental uses."
    },
    {
      "heading": "27.60.050 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.60.050",
      "text": "No horses, cattle, or other domestic animals shall be bred, raised, or maintained within 500 feet of any residential district as established in this zoning title."
    },
    {
      "heading": "27.60.060 LANDS EMBRACED.",
      "id": "/us/ca/cities/san-mateo/code/27.60.060",
      "text": "All land not contained within any other district established in this chapter shall be classified as open space embraced within such district as hereinafter provided."
    },
    {
      "heading": "27.60.070 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.60.070",
      "text": "The Open Space (OS) is established to provide areas for public and quasi-public open space and recreation purposes, noncommercial private open space and recreation uses, and to ensure continuing maintenance of open space for public safety, health and welfare."
    },
    {
      "heading": "27.60.080 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.60.080",
      "text": "Permitted uses shall be as follows: (a) Parks, playgrounds, community centers and facilities, publicly owned; (b) Vacant land for open space preservation"
    },
    {
      "heading": "27.60.090 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.60.090",
      "text": "The following uses may also be allowed if a special use permit is approved: (a) Detached accessory structures, other than secondary units, containing more than two plumbing fixtures or waste lines; (b) Swimming pools, hot tubs and spas located in required front yard or street side yard; (c) Secondary units subject to provisions of Chapter 27.19; (d) Cemeteries and mausoleums; (e) Churches, convents, parish houses, and monasteries; (f) Community services, including, but not limited to, libraries, parks, playgrounds, and community centers; (g) Public and private educational facilities; (h) Day care centers serving more than six persons or family day care centers serving more than 14 children; (i) Philanthropic and eleemosynary uses; (j) Public utility facilities; and (k) Temporary real estate sales offices for a period not to exceed the duration of the construction and sale of homes within the subdivision wherein the sales office is to be located."
    },
    {
      "heading": "27.60.100 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.60.100",
      "text": "The Qualified (Q) Overlay District is established to provide for development of land pursuant to standards and regulations which reflect the unique characteristics of a site. Any zoning plot which is classified Q shall retain its underlying classification unless otherwise provided for in this section."
    },
    {
      "heading": "27.60.120 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.60.120",
      "text": "Conditions of use may be imposed beyond those required by the underlying zoning. Such conditions shall be recorded in a manner satisfactory to the City Attorney and shall run with the land."
    },
    {
      "heading": "27.60.140 LAND USE STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.60.140",
      "text": "Except as otherwise provided for in this section, the land use standards of the underlying zone shall apply to uses developed subject to the Q Overlay District."
    },
    {
      "heading": "27.60.160 PLANNING APPLICATION SUBMITTAL.",
      "id": "/us/ca/cities/san-mateo/code/27.60.160",
      "text": "A planning application (PA) shall be submitted for any development of land pursuant to Q Overlay District standards and the standards of underlying zoning. Such planning application may be further conditioned as allowed by all applicable laws, codes, standards, policies and regulations."
    },
    {
      "heading": "27.60.180 QUALIFIED (Q) OVERLAY ZONING DISTRICTS.",
      "id": "/us/ca/cities/san-mateo/code/27.60.180",
      "text": "(a) Q1 (Qualified Overlay District 1)—Limitations and Conditions. The following limitations and conditions shall pertain to the use of property zoned Q1: (1) Location of Structures. Permanent structures or improvements, such as parking, landscaping or open space may be constructed south of the ramp connecting northbound Highway 101 and eastbound Highway 92 only when they are not required to fulfill zoning requirements of adjacent properties. (2) Access. No additional curb cuts shall be permitted beyond those existing on the site as of February 1, 1987. (3) Residential Use. Residential use is prohibited. (4) Parking. Parking on this site, with the exception of the provisions of Section 27.60.100 may be used to fulfill parking requirements for adjacent parcels. (5) Height Limitation. No structure shall exceed the height of the adjacent elevated freeway as measured to the top of the freeway railing. (6) Floor Area Ratio. The maximum allowed floor area ratio is 0.5. (b) Q2 (Qualified Overlay District 2)—Limitations and Conditions. The following limitations and conditions shall pertain to the use of property zoned Q2: (1) Lagoon Access. Public access to and along Marina Lagoon shall be provided, improved and maintained consistent with the Shoreline Park Specific Plan and requirements of the Landscape Resources Division and Public Works Department. (2) Parking. Parking on this site may be used to fulfill parking requirements for adjacent parcels. (3) Height Limitation. No structure shall exceed the height of the adjacent elevated freeway as measured to the top of the roadway railing. (4) Recreational vehicle storage facilities may be allowed subject to the approval of a special use permit under the provisions of Section 27.64.267 of this title. (5) Floor Area Ratio. The maximum allowed floor area ratio is 1.0. (c) Q3 (Qualified Overlay District 3)—Limitations and Conditions. The following limitations and conditions shall pertain to the use of property zoned Q3: (1) Required Yards. A landscaped 30-foot building setback and a 15-foot parking setback from the edge of the shoulder of Fashion Island Boulevard shall be provided. All landscaping shall be subject to the approval of the Landscape Resources Division. (2) Access. No curb cuts shall be permitted from Fashion Island Boulevard. (3) Parking. Parking on this site may be used to fulfill parking requirements for adjacent parcels. (4) Height Limitation. No structure shall exceed the height of the adjacent elevated freeway as measured to the top of the roadway railing. (5) Recreational vehicle storage facilities may be allowed subject to the approval of a special use permit under the provisions of Section 27.64.267 of this title. (6) Floor Area Ratio. The maximum allowed floor area ratio is 0.5. (d) Q4 (Qualified Overlay District 4)—Limitations and Conditions. The following limitations and conditions shall pertain to the use of property zoned Q4: (1) Accessory Use. Parking of passenger automobiles shall be permitted only when accessory to abutting nonresidential uses. (2) Parking. Parking on the site may be used to fulfill parking requirements for adjacent parcels. (3) Height Limitation. No structure shall exceed the height of the adjacent elevated freeway as measured to the top of the roadway railing. (4) Recreational vehicle storage facilities may be allowed subject to the approval of a special use permit under the provisions of Section 27.64.267 of this title. (5) Floor Area Ratio. The maximum allowed floor area ratio is 1.0. (e) Q5 (Qualified Overlay District 5)—Limitations and Conditions. The following limitations and conditions shall pertain to the use of property zoned Q5. Q5 is the portion of the Hillsdale Shopping Center on the east and west side of El Camino Real (i.e., Sub-Areas A, B, C and D).  (1) Projects which involve less than 75% demolition and/or expansion and/or redevelopment of structures (including parking structures) in Sub-Area A or Sub-Area B or Sub-Area C or Sub-Area D, and which require a Site Plan and Architectural Review (SPAR) as per Section 27.08.030, will be required to meet the following findings in addition to findings in Section 27.08.030(a)(1)—(5): (i) The development facilitates the safe and efficient flow of traffic balanced with enhanced opportunities for public transit and a safe pedestrian environment along and across El Camino Real; (ii) The development is compatible with existing retail uses, provides increased density of development near transit nodes, and contributes to a mix of uses along the corridor; (iii) The development enhances the district's identity as a focal point along El Camino Real by providing high-quality architecture, landscaping and signage, and promoting pedestrian-oriented activity; (iv) The development enhances the streetscape with high-quality landscaping sidewalks, street furniture, signage, entry features, and in the case of Sub-Area A, B, and D, theme intersection improvements at 31st Avenue, and improved connections and amenities for transit riders; and (v) The development promotes a healthy, vibrant business environment and complements the existing businesses and uses along El Camino Real. (2) When 75% or more demolition and/or expansion and/or redevelopment of structures (including parking structures) occurs in Sub-Area A, B, C or D, a comprehensive master plan for such sub-area(s) which is consistent with the El Camino Real Master Plan and Hillsdale Station Area Plan is required. The development will be required to meet the findings in Section 27.60.160(e)(1)(i)—(v) in addition to findings in Section 27.08.030(a)(1)—(5). (f) Q6 (Qualified Overlay District 6)—Limitations and Conditions. The following limitations and conditions shall pertain to the use of the property zoned Q6: (1) Uses. All uses in this district shall require a special use permit, as set forth in Chapter 27.74 of the Zoning Code. (2) Development. Future development in this district shall substantially comply with the conceptual development plan submitted as part of Planning Application #01-154 and as subsequently approved by the City Council on March 3, 2003. (3) Floor Area Ratio. This district shall have a maximum floor area ratio of 0.37:1. For the purposes of this district to calculate floor area, the size of the site is 557,568 square-feet. (g) Q7 (Qualified Overlay District 7)—Limitations and Conditions. The following limitations and conditions shall pertain to the use of the property zoned Q7: (1) Uses. All uses in this district shall require a special use permit, as set forth in Chapter 27.74 of the Zoning Code. (2) Development. Future development in this district shall substantially comply with the St. Matthew Parish Master Plan and Special Use Permit submitted as part of Planning Application #10-060 and as subsequently approved by the City Council on January 22, 2013. (3) Floor Area Ratio. This district shall have a maximum floor area ratio of 0.31. For the purposes of this district to calculate floor area, the size of the site is 310,400 square feet. For purposes of this zoning district, FAR will be calculated per zoning plot and not per parcel. (4) Parking. In conformance with the master plan, this district shall allow the establishment of 12 new parking spaces which backout directly onto Notre Dame Avenue. This is in addition to the 21 existing spaces that backout onto Notre Dame Avenue. (h) Q8 (Qualified Overlay District 8)—Limitations and Conditions. The following limitations and conditions shall pertain to the use of the property zoned Q8: (1) Uses. All uses in this district shall require a special use permit, as set forth in Chapter 27.74 of the Zoning Code. (2) Development. Future development in this district shall comply with the approved site plan and approved Special Use Permit as part of the Planning Application # PA2018-069 approved by the City of San Mateo. (3) Floor Area Ratio. This district shall have a maximum floor area ratio of 0.39. (4) Parking. Off-site parking facilities shall not be located in excess of 1,000 feet from the project site."
    }
  ],
  "Chapter 27.61 SC DISTRICTS—SENIOR CITIZEN OVERLAY DISTRICT—SPECIAL USE PERMITS": [
    {
      "heading": "27.61.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.61.010",
      "text": "The senior citizen overlay district is established to provide for development of land for senior citizen housing pursuant to standards which reflect the unique character of senior citizen residential occupancy. Any zoning plot classified as SC shall retain its existing, underlying classification and may be developed and used either pursuant to regulations pertaining to such underlying classification or, when authorized by a special use permit, pursuant to regulations pertaining to the senior citizen district."
    },
    {
      "heading": "27.61.020 LANDS SUBJECT TO SC OVERLAY CLASSIFICATION.",
      "id": "/us/ca/cities/san-mateo/code/27.61.020",
      "text": "The SC overlay classification may be superimposed only on these lands classified as R3, R4, R4-D, R5, R5-D, and R6-D, C (including CBD), E or TOD."
    },
    {
      "heading": "27.61.030 EFFECT OF DEVELOPMENT AND/OR USE PURSUANT TO SC REGULATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.61.030",
      "text": "Any zoning plot developed or used pursuant to SC regulations shall not thereafter be used for any purpose other than the provisions of senior citizen housing unless and until the zoning administrator has certified in writing that the alternate use satisfies all applicable land use regulations pertaining to the underlying classification of the zoning plot."
    },
    {
      "heading": "27.61.040 SENIOR CITIZEN HOUSING SPECIAL USE CRITERIA.",
      "id": "/us/ca/cities/san-mateo/code/27.61.040",
      "text": "Senior citizen housing may be permitted as a special use in SC overlay district, when the proposed use meets all of the following criteria: (1) Residential occupancy shall be limited to senior citizens 62 years of age or older, or 55 years of age or older in a senior citizen housing development, and qualified permanent residents, all as defined in California Civil Code Sections 51.2-51.4, or any successor legislation. (2) The impact of the use will be substantially equivalent to those impacts produced by uses otherwise allowed for land within the underlying classification of the zoning plot, with considerations being given to the type of the living units, number of living units, the probable number of residents and the demand on public facilities and services generated. (3) The location, size, design, and operating characteristics of the use will be compatible with and will not adversely affect the livability or appropriate development of abutting properties and the surrounding neighborhood, with consideration to be given to harmony in scale, bulk, coverage, and density; to the availability of civic facilities and utilities; to harmful effect, if any, upon desirable neighborhood character; to the generation of traffic and the capacity of surrounding streets; and to any other relevant impacts of the use. (4) The location, design, and site planning of the use will provide a convenient and functional living, working, shopping, or civic environment, and will be attractive as the nature of the use and its location and setting warrant. (5) The use will enhance the successful operation of the surrounding area in its basic community function, or will provide an essential service to the community or region. (6) Housing shall be specifically designed for the elderly and include facilities generally associated with the needs and interests of aged persons. Such facilities shall include common meeting and recreation facilities, secure parking areas, safety bars and rails in units, emergency signal system, adequate exterior lighting for security, ramps and other provisions required for elderly persons by State law or federal regulation. In addition, such facilities may include central dining facilities, laundry rooms, other convenience facilities for occupants, meeting and activity facilities for use by senior citizens from the surrounding community, and other facilities for the convenience of the senior residents. (7) The use will be so located as to provide residents easy access to community services such as transportation, shopping, and other daily services. Where appropriate, there should also be provided a generous amount of activity facilities (both indoors and outdoors) for residents."
    },
    {
      "heading": "27.61.050 SPECIAL DWELLING STANDARDS FOR SENIOR CITIZEN USES.",
      "id": "/us/ca/cities/san-mateo/code/27.61.050",
      "text": "Notwithstanding any other provision of this code, the minimum floor area for each residential unit for senior citizen use shall be as follows: (a) Bachelor or studio-type dwelling units four hundred five square feet; (b) One-bedroom dwelling units: (1) Five hundred seven square feet (if kitchen-dining and living areas combined); (2) Five hundred sixty-one square feet (if kitchen-dining and living areas separated); (c) Two-bedroom dwelling units: (1) Six hundred two square feet (if kitchen-dining and living areas combined); (2) Six hundred sixty-six square feet (if kitchen-dining and living areas separated)."
    },
    {
      "heading": "27.61.060 SPECIAL PARKING STANDARDS FOR SENIOR CITIZEN USES.",
      "id": "/us/ca/cities/san-mateo/code/27.61.060",
      "text": "Notwithstanding any other provision of this code, the number of parking spaces required to be provided for senior citizen uses may be as low as 0.25 spaces per rental dwelling unit and as low as 1.0 spaces per sale dwelling units. The actual ratio shall be determined at the time of granting the special use permit for the use. Ten percent of such spaces shall be designated handicapped parking stalls. In determining the number of parking spaces required, the following factors, as well as any other relevant factors, shall be considered: (1) The number of employees required by the use, whether such employees will reside on the premises, and hours during which any nonresident employees will be employed; (2) The availability of public transportation; (3) Whether residents of the use will be eligible for government rent subsidies; (4) The degree to which on-site provision of services and facilities will effect the need of residents to leave the site; (5) The proximity of facilities and services to the site. Where appropriate, employee parking on the site shall be separately identified and shall be available only to employees."
    },
    {
      "heading": "27.61.080 SPECIAL LOT AREA STANDARDS FOR SENIOR CITIZEN HOUSING.",
      "id": "/us/ca/cities/san-mateo/code/27.61.080",
      "text": "Notwithstanding any other provision of this code, the unit density of senior citizen housing uses shall be governed by the population density established by the special use permit, but in no case shall the land area per unit be less than three hundred fifty square feet. All other land use standards in these Districts still apply."
    },
    {
      "heading": "27.61.090 PARKING AND DWELLING STANDARDS FOR RESIDENT EMPLOYEES.",
      "id": "/us/ca/cities/san-mateo/code/27.61.090",
      "text": "Parking and dwelling unit standards for resident employees whose employment is the principal reason for residency shall be identical to those pertaining to multiple dwelling units throughout the City."
    },
    {
      "heading": "27.61.100 OTHER LAND USE STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.61.100",
      "text": "Except as provided in this chapter, the land use standards for senior citizen uses in those zoning plots whose underlying classifications are R3, R4, R4-D, R5, R5-D or R6-D shall be those pertaining to such underlying districts. Senior citizen uses on zoning plots whose underlying classifications are C or E shall, except as provided in this chapter or in the Downtown Specific Plan, be governed by the land use standards pertaining to the R5 district."
    },
    {
      "heading": "27.61.110 SENIOR CITIZEN USE GUARANTEES.",
      "id": "/us/ca/cities/san-mateo/code/27.61.110",
      "text": "Prior to occupancy of any zoning plot developed pursuant to senior citizen regulations, the project's proponent shall provide documentation limiting the use of the project to senior citizen housing exclusively and vesting in the City the right to enforce such limitation until and unless it determines that any proposed alternate use complies fully with regulations pertaining to the underlying district. Such documentation may consist of subdivision or parcel map dedication, covenants, conditions and restrictions pertaining to the zoning plot or a recordable use restriction. Any such documentation shall be in a form satisfactory to the City Attorney."
    },
    {
      "heading": "27.61.120 APPLICATION PROCEDURES.",
      "id": "/us/ca/cities/san-mateo/code/27.61.120",
      "text": "Except for reclassification initiated by the Planning Commission or City Council, all applications for SC classification shall be accompanied by a complete application for a senior citizen special use permit. Submittal requirements for senior citizen special use permits shall be identical to those provided for in this title for other special use permits, except for those additional matters required by the senior citizen regulations."
    }
  ],
  "Chapter 27.62 PLANNED DEVELOPMENTS—SPECIAL USE PERMITS": [
    {
      "heading": "27.62.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.62.010",
      "text": "This special permit is intended to enable and encourage flexibility of design and development of land in such a manner as to promote its most appropriate use; to allow diversification in the relationship of various uses, structures and space; to facilitate the adequate and economical provision of streets and utilities; to preserve the natural and scenic qualities of open space; to offer recreational opportunities close to home; to enhance the appearance of neighborhoods through preservation of natural green spaces, and to counteract the effects of urban congestion and monotony. The proposed development must be designed to provide an environment of a stable and desirable character, and must provide permanently reserved useable open space and areas for off-street parking adequate for the occupancy proposed. In residential development, it must include provision for open space and recreation areas to meet the needs of the anticipated population."
    },
    {
      "heading": "27.62.020 TYPES OF DEVELOPMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.62.020",
      "text": "There are created hereby two basic types of development: (1) Residential (2) Nonresidential. Where the type of planned unit development is not clear on the face of the application, it shall be determined by the zoning administrator."
    },
    {
      "heading": "27.62.030 GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.62.030",
      "text": "Where the planned unit development is determined to be residential, it shall be governed by the provisions of Sections 27.62.040 through 27.62.100."
    },
    {
      "heading": "27.62.040 ALLOWED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.62.040",
      "text": "Uses not specified as permitted, accessory or special uses by the use regulations of the zoning district in which the property is located may be allowed as part of a planned unit development provided: (1) The uses allowed hereby are necessary or desirable and are appropriate with respect to the basic type of development; (2) The uses permitted hereby are not of such a nature, or so located as to exercise a detrimental influence on the surrounding neighborhood; (3) Uses permitted hereby shall not be so extensive as to become the dominant purpose of the planned unit development."
    },
    {
      "heading": "27.62.050 DENSITY (RESIDENTIAL PD).",
      "id": "/us/ca/cities/san-mateo/code/27.62.050",
      "text": "The number of dwelling units shall be based on the minimum development standards for the zoning district in which the development is located. If the development is located in a nonresidential zone, R5 minimum development standards shall apply."
    },
    {
      "heading": "27.62.055 LOT SIZE AND WIDTH.",
      "id": "/us/ca/cities/san-mateo/code/27.62.055",
      "text": "(a) The lot size and width requirements of the underlying zone shall apply unless the proposed development site is over one acre in size and it can be demonstrated that: (1) A better design will be achieved by not adhering to Zoning Code requirements by: (A) Preserving and enhancing existing site elements such as, but not limited to, heritage trees, topography, waterways, important historical or architectural resource, views, natural open space and archaeological sites; or (B) Providing common open space and recreational facilities sufficient to meet the needs of the intended inhabitants; and (2) Adherence to the requirements of the Zoning Code is not required in order to insure the health, safety, and welfare of inhabitants of the development or adjacent properties. (b) Regardless of the approved lot size and width, in no case shall the residential planned unit development exceed the unit density development standards of the underlying zone."
    },
    {
      "heading": "27.62.060 SETBACKS AND SPACING BETWEEN BUILDINGS.",
      "id": "/us/ca/cities/san-mateo/code/27.62.060",
      "text": "(1) Setbacks and Distances Between Buildings Within the Development. Spacing and distances between principal buildings shall be at least equivalent to that required by the zoning district unless the applicant demonstrates that: (a) A better or more appropriate design can be achieved by not applying the provision of the zoning district; and (b) Adherence to the requirements of the zoning district is not required in order to insure health, safety and welfare of the inhabitants of the development. (2) Peripheral Setbacks. (a) Generally. Setbacks between any principal building and any peripheral boundary of the development shall be equal to the minimum required setback on the immediately adjacent property unless otherwise provided. (b) Decreased Setbacks. Decreased setbacks may be allowed where the applicant demonstrates that a better or more appropriate design can be achieved by the allowance of a reduced setback and adherence to the setback requirements of immediately adjacent property is not required in order to insure the health, safety and welfare of inhabitants of the development or the adjacent property. (c) Increased Setbacks. Setbacks greater than those of the immediately adjacent property may be required where the intensity of development is greater than that of the adjacent property to such an extent that greater peripheral setbacks are needed in order to insure the health, safety and welfare of the inhabitants of the development of the adjacent property."
    },
    {
      "heading": "27.62.070 CIRCULATION AND PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.62.070",
      "text": "(1) Major and local streets, the location of all buildings, parking areas, pedestrian ways, and utility easements, shall be designed to promote the public safety, compatibility of uses, and minimization of land use conflicts. (2) Private streets may serve circulation and parking purposes if designed for fire and police protection, rubbish collection, and lighting and other public services. (3) Circulation and parking areas shall be separated from recreational areas to facilitate safe vehicular movement. In the design of the circulation and parking plan, priority shall be given to pedestrian access and activity. (4) Driveways, circulation roadways and parking areas shall be designed to minimize traffic and congestion within the planned unit development, to minimize the amount of paving and to provide reasonable distribution of resident and visitor stalls to minimize walking distances. (5) Adequate access for fire and other emergency vehicles shall be provided on site. (6) Parking shall be provided which is equal to that required by Chapter 27.64 of this title, except that those requirements may be increased or decreased where the City Council determines that because of the location of the property with respect to surrounding areas within reasonable walking distance, and/or public transportation, or any other consideration reasonably relating to the need for parking in the development, such increase or decrease is appropriate. Where parking on private streets is unavailable or prohibited due to design or privately-enforced restrictions, parking requirements may be increased. (7) Legal notices for applications for planned unit development shall specify any reduction in parking which has been requested. (8) Communal parking areas shall be screened from living areas within the development by landscaping and transitional yards. (9) Where open parking areas are to be located immediately adjacent to any peripheral boundary, a separation or buffer of a type sufficient to insure the privacy of the adjacent property shall be provided. (10) Facilities shall be provided for the storage of recreational vehicles, such as boats, campers, and trailers where appropriate. (11) All streets which are part of the project shall be privately-owned and maintained, and shall provide continuous public access. The hours of public access may be reduced subject to the commission establishing the following findings: (A) Police, fire, and emergency matters or services shall not be adversely affected; (B) Public access shall not be substantially restricted; (C) Adjacent developments shall not be adversely affected; and (D) Public circulation in the area shall not be impaired."
    },
    {
      "heading": "27.62.080 LAND COVERAGE AND OPEN SPACE.",
      "id": "/us/ca/cities/san-mateo/code/27.62.080",
      "text": "(1) Floor Area Ratio. The floor area ratio (F.A.R.) of the zoning district in which the property is located shall apply unless the following conditions exist: (a) Applicant's plans demonstrate that better design will be achieved through allowance of increased floor area; (b) The increase in floor area allowed will not have a detrimental effect on surrounding property. (2) Open Space. Open space for recreational purposes must be provided which in terms of area and suitability will meet the needs of the inhabitants. In determining the requirement of open space, the following shall be considered: (a) The Park and Recreation Element of the General Plan; (b) The composition of the anticipated population of the development; (c) Such other factors and considerations which bear a reasonable relationship to the question of need for open space therein. (3) The City Council may, by resolution, promulgate such standards and policies for open space in residential planned developments as are deemed appropriate and in the furtherance of the health, safety and welfare of the future inhabitants and the community. (4) Open Space Standards and Requirements. Total common open space shall be equal to a minimum of 6 acres per 1,000 population for all residential planned developments. Common open space shall consist of the following: (a) Residential Common Usable Open Space. At least fifty percent (50%) of the required open space shall be usable open space, accessible to all occupants of the residential planned development. This may include landscaped areas devoted to recreational purposes accessible to all residents of the development. Swimming pools, recreation rooms and buildings, court game areas, plazas, play area, picnic areas, walkways in common areas and other common recreation facilities may also be used to fulfill this requirement. Landscape areas fulfilling this requirement shall be at least 450 sq. ft. in size, not less than ten feet in any dimension and shall not exceed twenty-five percent (25%) in slope. (b) Natural Area Landscaping. Up to fifty percent (50%) of the required open space may be provided in natural area landscaping. This includes preservation and enhancement of existing site elements, such as, but not limited to: heritage trees, major vegetation, waterways and unique topographic features. Decorative landscaping within these areas may be also used to fulfill this requirement. Areas fulfilling this requirement shall be at least 100 sq. ft. in size and not less than six feet in any dimension."
    },
    {
      "heading": "27.62.090 MAINTENANCE AND UTILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.62.090",
      "text": "(1) For each area to be held under common ownership, a document showing the future maintenance provisions shall be submitted for review with the application. Such provisions shall include mandatory membership of all property owners in any association designed for maintenance of the open space. (2) Where local open spaces are to be conveyed to the City in fee, the developer shall convey them at the stage and in the condition agreed upon in connection with processing and approval of the application. (3) In the event that the application results in a subdivision map showing lands available for park, recreation, open space, or other municipal purposes, the City Council, as a condition of approval of the application, may establish such conditions on the ownership, improvement, use, and maintenance of such lands as it deems necessary to assure the preservation of such lands for their intended purpose."
    },
    {
      "heading": "27.62.100 LANDSCAPING.",
      "id": "/us/ca/cities/san-mateo/code/27.62.100",
      "text": "Landscaping for setbacks, parking areas, open space and any other area of the development shall be required in accordance with applicable standards and policies promulgated heretofore or hereafter by resolution of the City Council."
    },
    {
      "heading": "27.62.110 GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.62.110",
      "text": "Where the planned unit development is determined to be nonresidential, it shall be governed by the provisions of Sections 27.62.120 through 27.62.180."
    },
    {
      "heading": "27.62.120 ALLOWED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.62.120",
      "text": "Uses not specified as permitted, accessory or special uses by the use regulations of the zoning district in which the property is located may be allowed as part of a planned unit development provided: (1) The uses allowed hereby are necessary or desirable and are appropriate with respect to the basic type of development; (2) The uses permitted hereby are not of such a nature, or so located as to exercise a detrimental influence on the surrounding neighborhood."
    },
    {
      "heading": "27.62.130 SETBACKS AND SPACING BETWEEN BUILDINGS.",
      "id": "/us/ca/cities/san-mateo/code/27.62.130",
      "text": "(1) Setbacks and Distances Between Buildings Within the Development. Spacing and distances between principal buildings shall be at least equivalent to that required by the zoning district unless the applicant demonstrates that: (a) A better or more appropriate design can be achieved by not applying the provision of the zoning district; and (b) Adherence to the requirements of the zoning district is not required in order to insure health, safety and welfare of the inhabitants of the development."
    },
    {
      "heading": "27.62.140 CIRCULATION AND PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.62.140",
      "text": "(1) Major and local streets, the location of all buildings, parking areas, pedestrian ways, and utility easements shall be designed to promote the public safety, compatibility of uses, and minimization of land use conflicts. (2) Private streets may serve circulation and parking purposes if designed for fire and police protection, rubbish collection, lighting, and other public services. (3) Adequate access for fire and other emergency vehicles shall be provided on site. (4) Parking requirements shall be equal to the sum of the parking requirements for all uses proposed. However, where it can be demonstrated by the applicant that due to nonconflicting hours of operation, design of the circulation and parking plan, or any other factor reasonably related to the need for parking the total parking requirement can be reduced, the Council may do so provided legal notice of the application specifies that such reduction has been requested. (5) Driveways and circulation roadways shall be designed to minimize traffic and congestion within the planned unit development and to minimize the amount of paving. (6) Where open parking areas are to be located immediately adjacent to any peripheral boundary, a separation or buffer of a type sufficient to insure the privacy of the adjacent property shall be provided. (7) All streets which are part of the project shall be privately-owned and maintained, and shall provide continuous public access. The hours of public access may be reduced subject to the commission establishing the following findings: (A) Police, fire, and emergency matters or services shall not be adversely affected; (B) Public access shall not be substantially restricted; (C) Adjacent developments shall not be adversely affected; and (D) Public circulation in the area shall not be impaired."
    },
    {
      "heading": "27.62.150 OPEN SPACE.",
      "id": "/us/ca/cities/san-mateo/code/27.62.150",
      "text": "Open space shall be provided in conformity with the standards specified for the central business district in Section 27.38.090. Landscaping of parking lots shall be provided in conformance with the standards set forth by council resolution requiring landscaping for all parking lots."
    },
    {
      "heading": "27.62.160 FLOOR AREA REGULATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.62.160",
      "text": "The floor area regulations (FAR) of the zoning district in which the property is located shall apply."
    },
    {
      "heading": "27.62.170 MAINTENANCE AND UTILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.62.170",
      "text": "For each area to be held under common ownership, a document showing the future maintenance provisions shall be submitted for review with the application. Such provision shall include mandatory membership of all property owners in any association designed for maintenance of the open space."
    },
    {
      "heading": "27.62.180 LANDSCAPING.",
      "id": "/us/ca/cities/san-mateo/code/27.62.180",
      "text": "Landscaping for setbacks, parking areas, open space and any other area of the development shall be required in accordance with applicable standards and policies promulgated therefor or hereafter by resolution of the City Council."
    },
    {
      "heading": "27.62.190 DEVELOPMENT PLAN—PREPARATION BY DESIGN GROUP.",
      "id": "/us/ca/cities/san-mateo/code/27.62.190",
      "text": "A development plan, prepared by a design group composed of at least three representatives of the following professions: (a) Architecture; (b) Landscape architecture; (c) Civil engineering, represented by a registered civil engineer; (d) Landplanning, represented by a full member of the American Planning Association."
    },
    {
      "heading": "27.62.200 DEVELOPMENT PLAN—CONTENT.",
      "id": "/us/ca/cities/san-mateo/code/27.62.200",
      "text": "A development plan shall consist of the following: (a) Uses and densities proposed; (b) Plot plans showing: (1) Location of buildings on the property, (2) Location of off-street parking, (3) Vehicle circulation, including that to be provided for fire and other emergency vehicles, (4) Areas devoted to open space and recreation, including a list of the facilities to be provided, (5) General provisions to be made for utilities and storm drains; (c) Grading plans, showing areas to be graded, cut or filled. The grading plan shall also show major vegetation to be removed and shall include an estimate of the amount of earth to be moved, imported and/or exported from the site; (d) Sections through property showing grades and building relationships thereto; (e) A description of the general scheme of architecture or architectural motif. Said description shall include schematic renderings where the zoning administrator deems it necessary or advisable; (f) A description of the general scheme of landscaping to be employed. Said description shall include schematic renderings where the superintendent of parks deems it necessary or desirable; (g) An indication of whether or not land is to be subdivided; (h) An indication of land to be dedicated for street, park, school or any other purpose; (i) A draft of major points of covenants proposed affecting the property; (j) A description of adjoining areas, uses or structures which may affect, or be affected by, the design or location of buildings of the development or the uses of traffic circulation therein; (k) A lighting plan including proposed street and security lighting, an analysis of the effect of such proposed lighting on adjacent property, and such other information as may reasonably be necessary; (l) A signing plan including the location, type, size, height and area of proposed signs."
    },
    {
      "heading": "27.62.210 DEVELOPMENT PLAN—REVIEW.",
      "id": "/us/ca/cities/san-mateo/code/27.62.210",
      "text": "The development plan shall be reviewed according to the following procedures, notwithstanding any other provisions of this code: Application for planned unit development shall be made to the Department of Community Development. All applications shall be in such form and shall be accompanied by such plans, documents and information as may be required. At the same time the Zoning Administrator may require that such other applications as are appropriate to the implementation of the plan be submitted, or he or she may require that they be submitted at a later date after approval of the development plan. Any such applications submitted with the plan will go forward to the Planning Commission and the City Council, and shall be effective only after action by the City Council. (a) Review by Planning Commission. Thereafter, the Planning Commission shall review the application hereunder and shall recommend to the City Council that the application be approved, approved with conditions, or denied. The Planning Commission shall hold a hearing on said application in accordance with the notice provisions of Section 27.06.050. (b) Review by City Council. Thereafter the Council shall review the application hereunder and shall approve, approve with conditions, or deny same. Notice of the Council hearing shall be given in accordance with the provisions of Section 27.08.050."
    },
    {
      "heading": "27.62.220 SUPPLEMENTARY ACTION.",
      "id": "/us/ca/cities/san-mateo/code/27.62.220",
      "text": "Following approval of concept, if such items have not been applied for in conjunction with development plan approval under Section 27.62.210, the applicant shall apply for site plan and architectural review and approval pursuant to Section 27.08.030 for each separate phase of building construction; site development permit, pursuant to Chapter 23.40 of this code; subdivision approval, where applicable, pursuant to Title 26 of this code; and heritage tree permit, where applicable, pursuant to Chapter 10.52 of this code, and any other applicable provision of this code."
    },
    {
      "heading": "27.62.230 DEVELOPMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.62.230",
      "text": "(1) Unless otherwise specified in the approval, special permits issued hereunder shall be governed by the time limitations of Section 27.08.060. In cases where the planned development concept includes development phases, every additional application necessary to complete the concept must be filed for not later than three years after the original council approval of the planned development concept, unless a longer time limit is authorized by the Council. Each such additional permit, as well as the special permit for the planned development, shall itself be governed by the time limitations of Section 27.08.060. The permit shall run with the land and may be exercised by the successor to the applicant. A further extension, for a period not to exceed one year, may be granted upon a proper showing that the delay in acting upon the approval granted has been occasioned by action or inaction of governmental agencies and is not due to delay or default on the part of the applicant. (2) When the City Council approves a planned development plan, building permits and certificates of occupancy may be issued in conformance with the plan so approved, provided that all other requirements of this code have been met. (3) No major modification of an approved development may be permitted without the approval by the City Council of the amendment to the special permit upon the recommendation of the Planning Commission after hearings duly held pursuant to the procedure hereinbefore set forth."
    }
  ],
  "Chapter 27.63 ADULT ENTERTAINMENT BUSINESSES": [
    {
      "heading": "27.63.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.63.010",
      "text": "The City Council finds that adult entertainment businesses, because of their very nature, are recognized as having objectionable operational characteristics, particularly when several of them are concentrated under certain circumstances, thereby having a deleterious effect upon the adjacent areas. Special regulation of these businesses is necessary to insure that these adverse effects will not contribute to blighting or downgrading of the surrounding neighborhoods. The primary purpose of this chapter is to prevent the concentration or clustering of these businesses in any one area."
    },
    {
      "heading": "27.63.020 DEFINITIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.63.020",
      "text": "(1) For purposes of this chapter, the \"adult entertainment businesses\" are defined as follows: (a) Adult Book Store. \"Adult book store\" means an establishment having as a substantial or significant portion of its stock in trade, books, magazines and other periodicals which are distinguished or characterized by their emphasis on matter depicting, describing or relating to specified sexual activities or specified anatomical areas, or an establishment with a segment or section devoted to the sale or display of such materials. (b) Adult Motion Picture Theater. \"Adult motion picture theater\" means an enclosed building with a capacity of fifty or more persons used for presenting material distinguished or characterized by their emphasis on matter depicting, describing or relating to specified sexual activities or specified anatomical areas for observation by patrons therein. (c) Adult Mini Motion Picture Theater. \"Adult mini motion picture theater\" means an enclosed building with a capacity for less than fifty persons used for presenting material distinguished or characterized by an emphasis on matter depicting or relating to specified sexual activities or specified anatomical areas for observation by patrons therein. (d) Adult Hotel or Motel. \"Adult hotel or motel\" means a hotel or motel wherein material is presented which is distinguished or characterized by an emphasis on matter depicting, describing or relating to specified sexual activities or specified anatomical areas. (e) Adult Motion Picture Arcade. \"Adult motion picture arcade\" means any place to which the public is permitted or invited wherein coin or slug-operated or electronically, electrically or mechanically controlled still or motion picture machines, projectors or other image-producing devices are maintained to show images to five or fewer persons per machine at any one time, and where the images so displayed are distinguished or characterized by an emphasis on depicting or describing specified sexual activities or specified anatomical areas. (f) Cabaret. \"Cabaret\" means a nightclub, theater or other establishment which features live performances by topless and/or bottomless dancers, \"go-go\" dancers, exotic dancers, strippers, or similar entertainers, where such performances are distinguished or characterized by an emphasis on specified sexual activities or specified anatomical areas. (g) Model Studio. \"Model studio\" means any business where, for any form of consideration or gratuity, figure models who display specified anatomical areas are provided to be observed, sketched, drawn, painted, sculptured, photographed, or similarly depicted by persons paying such consideration or gratuity. (h) Sexual Encounter Center. \"Sexual encounter center\" means any business, agency or person who, for any form of consideration or gratuity, provides a place where three or more persons, not all members of the same family, may congregate, assemble or associate for the purpose of engaging in specified sexual activities or exposing specified anatomical areas. (i) Strip Tease Establishment. \"Strip tease establishment\" means any place to which the public is admitted or invited which features live performances, fashion shows, or demonstrations intended to amuse or entertain patrons, and distinguished or characterized by an emphasis on the removal of clothing of the participants; provided, however, that this subsection shall have no application to fashion shows conducted in establishments whose principal business activity is the sale of goods other than food or drink for on-premises consumption. (j) Any other business or establishment which offers its patrons services or entertainment characterized by an emphasis on matter depicting, describing or relating to specified sexual activities or specified anatomical areas. (2) For the purposes of this chapter, \"specified sexual activities\" includes the following: (a) Actual or simulated sexual intercourse, oral copulation, anal intercourse, oral anal copulation, bestiality, direct physical stimulation of unclothed genitals, flagellation or torture in the context of a sexual relationship or the use of excretory functions in the context of a sexual relationship, and any of the following depicted sexually oriented acts or conduct: anilingus, buggery, coprophagy, coprophilia, cunnilingus, fellatio, necrophilia, pederasty, pedophilia, piquerism, sapphism, zooerasty; or (b) Clearly depicted human genitals in a state of sexual stimulation, arousal or tumescence; or (c) Use of human or animal masturbation, sodomy, oral copulation, coitus, ejaculation; (d) Fondling or touching of nude human genitals, pubic region, buttocks or female breast; or (e) Masochism, erotic or sexually oriented torture, beating or the infliction of pain, or (f) Erotic or lewd touching, fondling or other contact with an animal by a human being; or (g) Human excretion, urination, menstruation, vaginal or anal irrigation. (3) For purposes of this chapter, \"Specified anatomical areas\" include the following: (a) Less than complete and opaquely covered (1) human genitals, pubic region; (2) buttock; and (3) female breast below a point immediately above the top of the areola; and (b) Human male genitals in a discernibly turgid state, even if completely and opaquely covered."
    },
    {
      "heading": "27.63.030 SPECIAL REGULATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.63.030",
      "text": "(a) In those land use districts where the adult entertainment businesses regulated by this chapter would otherwise be permitted uses, it is unlawful to establish any such adult entertainment business if the location is: (1) Within five hundred feet of any area zoned for residential use; (2) Within one thousand feet of any other adult entertainment business; or (3) Within one thousand feet of any public or private school, park, playground, public building, church, any noncommercial establishment operated by a bona fide religious organization, or any establishment principally characterized by the offering of goods or services to minors. (b) The establishment of any adult entertainment business includes the opening or reopening (closed for any such reason) and any transfers of the business as a new business, the relocation of such business, or the conversion of an existing business location to any adult entertainment business use."
    }
  ],
  "Chapter 27.64 OFF-STREET PARKING AND LOADING": [
    {
      "heading": "27.64.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.64.010",
      "text": "The purpose of this chapter is to alleviate or prevent congestion of the public streets, and to promote the safety and welfare of the public by establishing minimum requirements for the off-street parking and loading and unloading of motor vehicles in accordance with the use to which property is put. In addition to the requirements of this chapter, all off-street parking shall conform to the requirements of the City \"Standard Drawings and Specifications\" as adopted by resolution of the City Council and on file with the public works department."
    },
    {
      "heading": "27.64.015 DEFINITIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.64.015",
      "text": "The following definitions apply to this chapter. (a) \"Aisle\" means the traveled path through a parking facility between one (1) or two (2) rows of parked vehicles. (1) \"Aisle width\" means the width of backout and driving aisle between parking rows. (2) \"Double-loaded traffic aisle\" means a driving aisle with accessible stalls on both sides. (3) \"Single-loaded traffic aisle\" means a driving aisle with accessible stalls on only one (1) side. (b) \"Angle of stall\" means the angle between the aisle direction and stall length direction. (c) \"Attendant parking\" means any facility which relies on attendants or valets, rather than the driver of the car, to park and unpark vehicles. (d) \"Bumper overhang\" means the area beyond the wheel stop and parking lot curbs where it is safe and legally permissible for bumpers to extend. (e) \"Carpool\" means a group of two (2) or more people who share their automobile transportation to the work place on a regular basis. (f) \"Depth of stall\" means the depth of a row or bay of parking measured perpendicular to the aisle regardless of the angle of parking. (g) \"Directional signs\" means signs placed in a parking facility that direct motorists to entrances, exits, aisles, ramps, bicycle storage, stairs, or elevators. (h) \"Employee parking\" means parking areas specifically designated for use by employees of uses on the lot. (i) \"Footcandle\" means a unit of illuminance on a surface that is everywhere on that surface one (1) foot from a uniform point source of light of one (1) candle and equal to one (1) lumen per square foot. (j) \"Head-in\" means a parking system where vehicles park hood first in the parking stall. (k) \"Layout dimension\" means the distance from stall to stall on centers measured parallel to the aisle. (l) \"Length of stall\" means the measurement of the individual stall measured perpendicular to the width. (m) \"Loading zone\" means a specially marked area for short term use of delivery vehicles. (n) \"Parking bay\" means the section of a parking facility containing an aisle and one (1) or two (2) rows of parking stalls. (o) \"Ramp\" means an inclined portion of a parking structure intended for travel purposes to access different levels or areas of a parking structure and which may provide parking stalls on one (1) or both sides. (p) \"Reservoir space\" means a space at least 20 feet long located in a parking facility for vehicles queuing to enter, exit or await service. (q) \"Stall\" means a portion of a parking facility designed to hold one (1) vehicle and marked by painted lines on pavement. (1) \"Back-in stall\" means an off-street parking stall into which the vehicle is backed from the driving aisle. (2) \"Clear stall\" means an off-street parking stall which has no structure or obstruction higher than a six (6) inch curb on either side. (3) \"Compact stall\" means an off-street parking stall that is eight (8) feet wide and 17 feet long that is designed to accommodate a vehicle which is less than 15 feet in overall length and six (6) feet in width. (4) \"Confined stall\" means an off-street parking stall which has any obstruction higher than a six (6) inch curb on both sides, including walls, railings, stairwells, columns, or fences, but excepting columns located more than seven (7) feet from aisles. (5) \"End stall\" means the last off-street stall in a row or bay of parking that requires a motorist to egress in the direction of ingress and requires additional backup space. (6) \"Restricted stall\" means an off-street parking stall which has any structural element, including curbs over six (6) inches, on either side. (7) \"Stall dimension\" means the length, width, and height of a parking stall. (8) \"Standard stall\" means an off-street parking stall that is eight (8) feet six (6) inches wide and 18 feet long. (r) \"Visitor parking\" means short term parking intended for use by customers or non-residents. (s) \"Wheel stops\" means a bumper or block placed at the head of a parking stall to restrain the vehicle from moving past the wheel stop. (t) \"Width of stall\" means the clear width of an individual stall measured perpendicular to the angle of parking."
    },
    {
      "heading": "27.64.020 SCOPE.",
      "id": "/us/ca/cities/san-mateo/code/27.64.020",
      "text": "This chapter shall apply as follows: (1) For all buildings and structures erected and all uses of land established after June 19, 1986, accessory parking and loading facilities shall be provided as required by the regulations of the district in which such buildings or uses are located. However, where a building permit has been issued prior to that date, and provided that construction is begun within six (6) months of such date and diligently prosecuted to completion, parking and loading facilities as required hereinafter need not be provided; (2) When the intensity of use of any building, structure or premises is increased through addition of dwelling units, gross floor area, seating capacity, or other units of measurement specified herein for required parking or loading facilities, parking and loading facilities shall be provided for such increase in intensity of use; (3) Whenever the existing use of a building, structure or premises is hereafter changed to a new use, parking or loading facilities shall be provided as required for such new use. However, if this building or structure was erected or use established prior to June 19, 1986, additional parking or loading facilities are mandatory only in the amount by which the requirements for the new use would exceed those for the existing use if the latter were subject to the parking and loading provisions of this title; (4) Whenever a parking lot is voluntarily upgraded without a change in or intensification of use, the parking lot shall reflect an improvement towards meeting the design provision of this chapter. Irrigation systems shall be required for any new planting areas proposed; (5) At the time of erection or enlargement of any building containing one (1) or more dwelling units, or the addition of one (1) or more dwelling units to or within an existing building, there shall be provided and maintained garage and parking spaces for each such new or added dwelling unit as required by this chapter. Each existing unit that does not comply with this chapter shall be provided with at least one (1) garage space. That portion of existing parking that exceeds the requirements of this chapter may be reassigned to the added units."
    },
    {
      "heading": "27.64.023 PARKING—PROHIBITED ON LAWNS, FLOWERS, SIDEWALK.",
      "id": "/us/ca/cities/san-mateo/code/27.64.023",
      "text": "It is unlawful to park a motor vehicle, trailer, unmounted camper or boat: (1) upon any lawn or landscaped area, including an area of flowers or shrubs; (2) upon an area of decorative rocks, stones, chips, bark, or the like, unless such area of decorative rocks, stones, chips or bark was in place and used for parking of a motor vehicle, trailer, unmounted camper or boat prior to July 19, 1993; or (3) upon the sidewalk, thereby impeding the pedestrian right-of-way. Nothing herein shall be construed to prohibit parking on a driveway. For this section, a driveway shall mean the area from the property line to the garage or carport. This provision shall apply to parcels being used for single-family or duplex residences."
    },
    {
      "heading": "27.64.025 DRIVEWAYS.",
      "id": "/us/ca/cities/san-mateo/code/27.64.025",
      "text": "New driveway access to arterial streets (as defined in the Circulation Element of the General Plan) is prohibited unless no other means of access is available. Existing curb cuts on arterial streets shall be eliminated in new developments whenever feasible. Access to garage space or parking space shall be provided by a driveway or driveways according to the following standards: (1) All Uses. (A) Driveways may not be less than 10 feet wide when serving two (2) or fewer garage or parking spaces, and not less than 12 feet wide when serving three (3) or more garage or parking spaces. (B) Each required off-street parking stall shall open directly upon an aisle or driveway of such width and design as to provide safe and efficient means of vehicular ingress and egress. All off-street parking facilities shall be designed with appropriate means of vehicular access to a street or alley in a manner which will least interfere with traffic movements, and shall provide a safe and efficient means for pedestrians using the parking facility to access the building entry. (2) Residential Uses. Residential driveways shall not exceed 20 lineal feet in width. If additional driveway width is desired in order to serve three (3) or more garage or parking stalls, the applicant shall submit appropriate plans for the approval of the Zoning Administrator and Director of Public Works. For more than one (1) curb cut on a parcel on any street frontage, at least 20 feet measured at top of curb shall be provided between each curb cut. (3) Nonresidential Uses. Driveways serving nonresidential uses shall not exceed 26 lineal feet in width at the street property line for each 50 feet of lot frontage upon a street, except that any lot having less than 50 feet street frontage may have but one (1) 20-foot driveway. In addition to the restrictions above, lots of more than 50 feet in width at the street line may have a total width of driveways at the front property line of no more than 52% of the total lot width abutting upon a street."
    },
    {
      "heading": "27.64.030 FACILITIES—EXISTING.",
      "id": "/us/ca/cities/san-mateo/code/27.64.030",
      "text": "Accessory off-street parking or loading facilities which are located on the same parcel as the building or use served and which were in existence on June 18, 1986 or were provided voluntarily after such date, shall not hereafter be reduced below, or if already less than, shall not further be reduced below the requirements of this title for a similar new building or use."
    },
    {
      "heading": "27.64.040 FACILITIES—PERMISSIBLE.",
      "id": "/us/ca/cities/san-mateo/code/27.64.040",
      "text": "Nothing in this title shall be deemed to prevent the voluntary establishment of off-street parking or loading facilities to serve an existing use of land or buildings provided that all regulations herein governing the location, design, improvement, and operation of such facilities are adhered to."
    },
    {
      "heading": "27.64.050 DAMAGE—DESTRUCTION.",
      "id": "/us/ca/cities/san-mateo/code/27.64.050",
      "text": "For any conforming building or use which is in existence on (date to be inserted), which is subsequently damaged or destroyed by fire, collapse, explosion or other cause, and for any legally nonconforming use which is lost by reason of such damage, and which is reconstructed, reestablished, or repaired, off-street parking or loading facilities need not be provided, except that parking or loading facilities equivalent to any maintained at the time of such damage or destruction shall be restored or continued in operation. However, in no case shall it be necessary to restore or maintain parking or loading facilities in excess of those required by this title for equivalent new uses or construction."
    },
    {
      "heading": "27.64.060 CONTROL OF OFF-STREET PARKING FACILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.060",
      "text": "The location of off-street parking facilities in relation to the use served shall be governed by the following provisions: (1) Residential Districts. Parking facilities accessory to dwelling units shall be located on the same parcel as the use served except as provided in Section 27.64.100. Spaces accessory to uses other than dwellings (such as churches) may be located on a plot adjacent to, or directly across a street or alley from the plot occupied by the use served if a special use permit is obtained from the Planning Commission; but in no case at a walking distance in excess of 200 feet from such use. (2) Nonresidential Districts. Parking facilities accessory to dwelling units shall be located on the same parcel as the use served, except as provided in Section 27.64.200. Parking facilities accessory to uses other than dwellings may be located on other than the same parcel as the use served (off-site) if a special use permit is obtained from the Planning Commission. Unless otherwise required, all required parking spaces shall be within a walking distance of 500 feet of the use served. No parking spaces accessory to a use in a commercial, executive, or manufacturing district shall be located in a residential district, unless authorized by the Planning Commission through a special use permit. (A) Where required parking facilities are provided on land other than the parcel on which the building or use served by such facilities is located, they shall be and remain in the same possession and ownership as that of the parcel occupied by the building or use to which the parking facilities are accessory except that the Planning Commission may authorize the use of leased, off-site land for the provision of required parking in either of the following cases: (i) The term of the lease approximates the expected life of the building or use to which the parking facilities are accessory and the lessor and the applicant acknowledge in writing recorded to the satisfaction of the City that a failure to continuously maintain the total number of spaces required shall require the immediate reduction of the intensity of the use served to the extent necessary to bring it into full conformance with the parking requirements of this chapter; or (ii) The number of required parking spaces leased for a shorter term does not exceed 25% of the total number of required parking spaces and the applicant and lessor acknowledge this restriction in writing as specified in subsection (i) above."
    },
    {
      "heading": "27.64.070 SUBMISSION OF PLOT PLAN.",
      "id": "/us/ca/cities/san-mateo/code/27.64.070",
      "text": "Any action involving the creation, expansion, or alteration of a parking lot, whether in conjunction with other approval requests or as an independent action, shall be subject to site plan and architectural review, unless the Zoning Administrator determines, based on a written justification and plot plan submittal, that the improvements are minor in nature, pursuant to Section 27.06.020. Minor site improvements include small parking lots containing 11 stalls or less."
    },
    {
      "heading": "27.64.080 USE OF PARKING AND GARAGE FACILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.080",
      "text": "Off-street assigned parking and garage facilities accessory to residential use and developed in any residential district in accordance with the requirements of this chapter shall be used solely for the storage of passenger automobiles or bicycles in-lieu of a vehicle, owned by occupants of the dwelling structures to which such facilities are accessory or by guests of said occupants. Under no circumstances shall required parking and garage facilities accessory to residential structures be used for the storage of commercial vehicles or for the parking of automobiles belonging to the employees, owners, tenants, visitors or customers of business or manufacturing establishments."
    },
    {
      "heading": "27.64.090 JOINT PARKING FACILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.090",
      "text": "Off-street parking facilities, for different buildings, structures or uses, or for mixed uses, may be provided collectively in any zoning district in which separate parking facilities for each constituent use would be permitted, provided that the total number of spaces so located together shall not be less than the sum of the separate requirements for each use."
    },
    {
      "heading": "27.64.100 PARKING ASSESSMENT AND SPECIAL DISTRICTS",
      "id": "/us/ca/cities/san-mateo/code/27.64.100",
      "text": "(a) Downtown Specific Planning Area—Central Parking and Improvement District (CPID). (1) Minimum Parking Requirements. Where a parcel of real property is located within the Central Parking and Improvement District, new projects to be located on said parcel shall either fund a City-commissioned project-specific parking demand study to determine the number of required parking spaces or meet the off-street parking requirements set forth below: (2) New Projects. New projects shall include the following: (A) New construction of buildings on a vacant or previously-built-upon parcel; (B) External expansion of existing buildings or established uses including all added floor area that creates need for additional parking; (C) New use in an existing building or structure with or without substantial internal renovation that results in a requirement for additional parking under the provisions of this chapter. (3) All new projects that enter into parking agreements with the CPID shall be subject to the assessment defined in current CPID resolutions. New projects as defined in subsections (2)(B) or (C) will be required to provide additional parking in the amount that the parking requirement caused by the expansion or new use exceeds the parking requirement established on June 19, 1986 as follows: (A) Properties within the Primary Benefit Zone shall provide required parking or pay parking in-lieu fees if the additional parking required exceeds 10 parking spaces; otherwise, a new project under subsection (2)(B) or (C) will cause the project property owner's parking deficiency under the current CPID assessment resolution to be increased by the number of additional parking spaces required by the new use or expansion or the number of existing and required parking spaces eliminated, or both. (B) Properties outside the Primary Benefit Zone shall provide required parking or pay parking in-lieu fees for any additional parking required as a result of a new project under subsections (2)(B) or (C) or the elimination of existing and required parking spaces, or both. (4) Limited Parking Zone (LPZ). Restrictions on parking in the limited parking zone in addition to other requirements of this chapter are as follows: (A) All Uses. New vehicular access to loading facilities, parking lots or structures and buildings is prohibited along street frontages within the limited parking zone. Existing curb cuts along street frontages in the LPZ shall be eliminated, unless the following requirements are met: (i) Curb cuts are needed for access to parking or loading facilities and do not negatively affect retail continuity or pedestrian safety; and (ii) A site plan and architectural review for the access is approved. (B) Residential Uses. Parking shall be provided as follows: (i) On-site, provided that vehicular access from a street in the limited parking zone is prohibited unless no other access is feasible and no remote parking facility such as leased spaces is available or can be made available within 200 feet; (ii) On a site outside the limited parking zone; or (iii) By lease or agreement with the City or CPID when a CPID parking facility is located within 200 feet. (C) Nonresidential Uses. Parking may be provided on-site in an amount not to exceed the required number of visitor stalls, subject to the approval of a special use permit. On-site parking in excess of the required visitor stalls may be allowed subject to approval of a special use permit where a new project meets one (1) of the following: (i) The parcel has primary access from a street outside the limited parking zone; or (ii) The parcel is located on a corner site which has a minimum lot area of 22,000 square feet or one-half the land area of the block in which the use is located, whichever is less. (D) Projects within the Limited Parking Zone may pay the City's parking in lieu fee for any required parking not provided on site. (5) Projects within the City's Central Parking Improvement District and outside of the Limited Parking Zone must satisfy a minimum of 25% of the project's required parking through provision of on-site parking. However, in order to prevent parking shortages in public parking facilities or neighboring residential zones, projects within the City's Central Parking Improvement District and outside of the Limited Parking Zone must satisfy a minimum of 50% of the project's required parking through provision of on-site parking when: (A) Public off-street parking occupancy within one-quarter mile of the proposed project location exceeds 85% at peak periods based on a parking study; or (B) The proposed project location is adjacent to areas zoned R-1, R-2, R-3, R-4, or R-5. (6) Parking Expansion Zone. Parking provided in addition to the minimum parking requirements may be leased to the CPID on a long term basis as public parking in accordance with a current CPID resolution. (7) Employee and Resident Parking. (A) New projects within the CPID shall provide required employee and resident parking by one (1) or more of the following means: (i) On-site, if located outside the limited parking zone; (ii) Off-site through construction or lease of private spaces, subject to approval of a special use permit; or (iii) By CPID lease, in-lieu fee payment, or parking agreement, as defined by a current CPID resolution, subject to availability. (B) Any nonresidential use outside the limited parking zone may reduce employee parking in accordance with the following: (i) Demonstration by the applicant that the amount of floor area per full-time equivalent employee exceeds the following due to unusual circumstances: (ii) A reduction in the employee parking requirement may be granted equal to the percentage difference between the lower employee density demonstrated by the applicant and the employee density standards delineated above. (8) Visitor and Customer Parking. New projects within the CPID may utilize the spaces provided by the CPID for the visitor and customer parking requirement, subject to assessment as defined by a current CPID resolution and availability of spaces. (9) Loss of Metered Parking. New projects which result in the loss of on-street metered CPID parking spaces shall compensate the CPID for the loss of metered parking by one (1) of the following: (A) Provide replacement stalls on-site within 200 feet of a new residential use or within 500 feet of a new non-residential use, to be made available for use by the public; (B) Compensation to the CPID for the cost of providing replacement parking, in accordance with a current CPID resolution; or (C) Approval of a special use permit by the Planning Commission, based on the finding that the improvements which necessitate the loss of metered parking spaces improve overall street circulation. (b) Downtown Specific Planning Area—Outside the Central Parking and Improvement District. Minimum off-street parking requirements for residential and non-residential uses shall be as specified in Sections 27.64.160 through 27.64.260. (c) 25th Avenue Parking District. Where a parcel of real property is located within the boundaries of the 25th Avenue motor vehicle off-street parking assessment district, a building or structure not to exceed one (1) story in height may be constructed and maintained on said parcel without provisions for, or maintenance of, off-street parking facilities for all executive and commercial uses. Off-street parking facilities shall be installed and maintained for each story in excess of one (1) story, so that the total number of parking spaces provided for the additional story or stories, shall meet the off-street parking requirements as specified herein. (d) Hillsdale Station Area. Where a parcel of real property is located within the Hillsdale Station Area Plan boundary, off-street parking is subject to the Station Area Parking Requirements listed in the Plan. In addition, all new development on such properties must prepare a Trip Reduction and Parking Management Plan as detailed in the Hillsdale Station Area Plan, including, but not limited to, Table 6-1, Station Area Parking Requirements."
    },
    {
      "heading": "27.64.110 COMPUTATION.",
      "id": "/us/ca/cities/san-mateo/code/27.64.110",
      "text": "When determination of the number of off-street parking spaces required by this title results in a requirement of a fractional space, an additional space shall be provided."
    },
    {
      "heading": "27.64.120 STALL DIMENSIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.64.120",
      "text": "All required off-street parking stalls shall have a vertical clearance, length and width in conformity with the requirements of the City \"Standard Drawings and Specifications\" and the following standards: (a) Width of stall shall conform to the requirements of the City \"Standard Drawings and Specifications.\" (b) Length of stall shall conform to the requirements of the City \"Standard Drawings and Specifications.\" (1) Stall depths may be reduced two (2) feet where bumper overhang is permissible. (c) Relationship of stall dimensions to aisle dimensions and parking angle shall be as outlined in the Standard Drawings and Specifications. (d) Existing substandard stalls shall be counted towards satisfying the off-street parking requirements of this chapter only where the dimensions equal or exceed those required for minimum compact car dimension. (e) Compact car stalls shall be clearly identified by marking the surface of each space: \"Compact.\" (f) All required off-street parking stalls shall have a vertical clearance of not less than seven (7) feet over the entire area, unless the stall is part of a mechanical parking system. Such stalls may have less than seven (7) foot clearance if otherwise consistent with City \"Standard Drawings and Specifications.\""
    },
    {
      "heading": "27.64.125 AISLE DIMENSIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.64.125",
      "text": "Aisles serving off-street parking stalls shall conform with the requirements of the City \"Standard Drawings and Specifications\" and the following standards: (a) Aisles parallel and adjacent to public sidewalks shall be separated by a landscape strip of at least six (6) feet. (b) One-way aisles shall alternate direction, or otherwise provide logical vehicular circulation subject to approval of the Director of Public Works. (c) Aisles shall provide for non-congestive flow from and into the street by logical relationships with the driveways. A two-way driveway shall directly connect with a two-way aisle. Reversal of the \"right-hand rule\" of driving for two-way aisles or closely adjacent one-way drives is prohibited. (d) One-way aisles shall not dead-end. (e) Circulation requiring use of the street or public right-of-way is prohibited."
    },
    {
      "heading": "27.64.130 TURNING RADII AND TURNAROUND REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.64.130",
      "text": "Circulation for parking facilities shall conform with the following standards: (a) Back out onto any public right-of-way shall be prohibited for all uses except single-family and two-family dwellings. (b) For all uses except single-family and two-family dwellings and secondary units, all parcels providing three (3) or more permanently maintained garage or parking stalls shall provide an area for turnaround purposes on the site which shall conform with the requirements of the City \"Standard Drawings and Specifications\" and be located adjacent to the entrance of the garage or parking stall, and not on any part of the public right-of-way. (c) No portion of a circular ramp may be considered as aisle for automobiles in adjacent bays. (d) Ramps in multi-level garages shall be designed with gradual slopes to ensure driver visibility of the pavement at all times, and shall be subject to approval of the Director of Public Works. (e) Turning aisles or ramps with two-way traffic shall have radii and aisle widths sufficient for two (2) automobiles to pass on the turn. Ramp widths on turns shall be as follows: (f) No portion of a circular ramp may be considered as aisle for automobiles in adjacent bays. (g) Ramps in multi-level garages shall be designed with gradual slopes to insure driver visibility of the pavement at all times, and shall be subject to approval of the Director of Public Works."
    },
    {
      "heading": "27.64.140 DESIGN—MAINTENANCE.",
      "id": "/us/ca/cities/san-mateo/code/27.64.140",
      "text": "(a) Lighting. Any lighting used to illuminate off-street parking areas shall be consistent with the City's Security Ordinance (Chapter 23.54) and otherwise be directed away from residential properties in such a way as not to create a nuisance. (b) Signs. Directional signs are permitted on parking areas in accordance with Title 25. (c) Repair and Service. No motor vehicle repair work of any kind shall be permitted on any off-street parking facilities. The sale of gasoline and motor oil in conjunction with accessory off-street parking or garage facilities is not permitted in any residence district."
    },
    {
      "heading": "27.64.150 FLOOR AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.64.150",
      "text": "Unless otherwise specified, the floor area used for determining off-street parking requirements is the floor area of the building(s) as defined in Section 27.04.200(c)."
    },
    {
      "heading": "27.64.160 PARKING SCHEDULES GENERALLY.",
      "id": "/us/ca/cities/san-mateo/code/27.64.160",
      "text": "For the following uses on property located outside the Downtown Specific Planning area, accessory off-street parking spaces shall be provided as listed below. Parking spaces required on an employee basis shall be based on the maximum number of employees on duty, or residing, or both, on the premises at any one time."
    },
    {
      "heading": "27.64.165 RESIDENTIAL USES; ADDITIONAL REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.64.165",
      "text": "Off-street residential parking shall comply with the following additional criteria: (a) All residential dwelling units shall be provided with the existing or required amount of off-street parking as a part of the sales, lease or rent agreement for the dwelling unit. (b) The proximity of the resident and visitor parking spaces to the dwelling units shall be as close as practicable. (c) Resident parking spaces shall be clearly marked or signed \"reserved.\" Visitors' parking spaces shall be clearly marked \"visitors only.\" (d) Both resident and visitor parking in uncovered and carport spaces shall be adequately lighted at night. Said lighting shall be designed to be directed away from adjacent residences. (e) Access to all off-street parking spaces shall be easily made without undue maneuvering to get into or out of the stall. All stalls shall be equally accessible. (f) Each room meeting the standard of The Building Code as a bedroom, shall be counted as a bedroom in determining parking requirements."
    },
    {
      "heading": "27.64.170 TRANSPORTATION SYSTEMS MANAGEMENT (TSM).",
      "id": "/us/ca/cities/san-mateo/code/27.64.170",
      "text": "New uses with 25 or more employees shall comply with the requirements of Chapter 24 of the San Mateo Municipal Code with regards to Transportation Systems Management."
    },
    {
      "heading": "27.64.185 AUTOMOBILE SERVICE STATIONS; ADDITIONAL REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.64.185",
      "text": "(a) Only vehicles awaiting service and towing vehicles shall be stored on the premises, with the exception of employee parking and approved rental parking spaces. (b) Parking of commercial vehicles shall be prohibited unless allowed in the zoning district as a permitted use."
    },
    {
      "heading": "27.64.260 MIXED OR MULTIPLE USES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.260",
      "text": "When two (2) or more uses are located on the same zoning plot or within the same building, parking spaces equal in number to the sum of the separate requirements for each such use shall be provided. No parking space or portion thereof shall serve as a required space for more than one (1) use unless otherwise authorized by the Planning Commission in accordance with Title 27. Chapters 27.06 through 27.12, 27.62, 27.74, 27.78 and 27.80."
    },
    {
      "heading": "27.64.262 BICYCLE PARKING FACILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.262",
      "text": "These bicycle parking requirements shall apply to the indicated activities as specified below. (a) Bicycle Parking Required for New and Existing Uses. Bicycle parking shall be provided for new development projects, additions to existing buildings, and new living units in existing buildings. Bicycle parking as prescribed hereafter shall be provided for activities occupying buildings, or portions of, which are constructed, established, wholly reconstructed, or moved onto a new lot, except to the extent that existing bicycle parking exceeds such requirements for any existing facilities. The required amount of new bicycle parking shall be based on the cumulative increase in floor area, or other applicable unit of measurement prescribed hereafter. If an existing building is altered or changed in occupancy so as to result in an increase in the number of residential living units, bicycle parking shall be provided for the new units. (b) More Than One (1) Activity on a Lot. Whenever a single lot contains different activities with the same bicycle parking requirement, the overall bicycle parking requirement shall be based on the sum of all such activities. Whenever a single lot contains activities with different bicycle parking requirements, the overall requirement shall be the sum of the requirements for each activity calculated separately. (c) Determination by Zoning Administrator. For uses not listed in the schedules of bicycle parking requirements, bicycle parking spaces shall be provided on the same basis as required for the most similar listed use, or as determined by the Zoning Administrator. (d) Standards for Required Bicycle Parking. (1) Types of Required Bicycle Parking. (A) Long-Term Bicycle Parking. Each long-term bicycle parking space shall consist of a locker or a rack located within a locked enclosure, such as a secure room or controlled access area, providing protection for each bicycle from theft, vandalism and weather. Long-term bicycle parking is meant to accommodate employees, students, residents, commuters, and others expected to park more than two (2) hours. (B) Short-Term Bicycle Parking. Short-term bicycle parking shall consist of a bicycle rack or racks and is meant to accommodate visitors, customers, messengers, and others expected to park not more than two (2) hours. (2) Minimum Specifications for Required Bicycle Parking. (A) All bicycle parking facilities shall be dedicated for the exclusive use of bicycle parking and shall not be intended for the use of motorized two-wheeled or similar vehicles. (B) All required short-term bicycle parking spaces shall permit the locking of the bicycle frame and one (1) wheel with a U-type lock, support the bicycle in a stable horizontal position without damage to wheels, frame, or components, and provide two (2) points of contact with the bicycle's frame. Art racks are subject to review by the Zoning Administrator. (C) All required long-term bicycle parking spaces, with the exception of individual bicycle lockers, shall permit the locking of the bicycle frame and one (1) wheel with a U-type lock and support the bicycle in a stable position without damage to wheels, frame, or components. (D) Bicycle parking facilities shall be securely anchored so they cannot be easily removed and shall be of sufficient strength and design to resist vandalism and theft. (E) The overall design and spacing of such facilities shall meet the standards of subsection (3). (3) Location and Design of Required Bicycle Parking. Required bicycle parking shall be placed on site(s) as set forth below: (A) A short-term bicycle parking space shall be at least two and one-half (2.5) feet in width by six (6) feet in length to allow sufficient space between parked bicycles. (B) Bicycle parking facilities shall not impede pedestrian or vehicular circulation. (i) Bicycle parking racks located on sidewalks should be kept clear of the pedestrian through zone. (C) Bicycle parking facilities are subject to the following standards: (i) Short-term bicycle racks shall be located with at least 30 inches clearance in all directions from any obstruction, including but not limited to other racks, walls, and landscaping. Large retail uses, supermarkets, and grocery stores are encouraged to locate racks with a 36-inch clearance in all directions from any vertical obstruction, including but not limited to other racks, walls, and landscaping. (ii) All bicycle facilities shall provide a minimum four (4) foot aisle to allow for unobstructed access to the designated bicycle parking area. (iii) All long-term bicycle parking facilities shall include a variety of rack types to accommodate different bicycle sizes, styles, and users, as determined by the Zoning Administrator. (D) Bicycle parking facilities within auto parking facilities shall be protected from damage by cars by a physical barrier such as curbs, wheel stops, poles, bollards, or other similar features capable of preventing automobiles from entering the designated bicycle parking area. (E) Short-term bicycle parking facilities serving community activity centers such as libraries and community centers should incorporate weather-protective enclosures shielding the designated bicycle area from typical inclement weather when feasible. (F) Bicycle parking facilities shall be located in highly visible well-lighted areas. In order to maximize security, whenever possible short-term bicycle parking facilities shall be located in areas highly visible from the street and from the interior of the building they serve (i.e., placed adjacent to windows). (G) The location and design of required bicycle parking shall be of a quality, character and color that harmonize with adjoining land uses. Required bicycle parking shall be incorporated whenever possible into building design or street furniture. (H) Long-term bicycle parking shall be covered and shall be located on site or within 200 feet of the main building entrance. The main building entrance is defined as publicly accessible entrances and shall exclude gated private garage entrances, trash room entrances, and other building entrances that are not publicly accessible. (I) Short-term bicycle parking must be along project frontage and within 50 feet of the main entrance to the building or commercial use or up to 100 feet where existing conditions do not allow placement within 50 feet. It should be in a well-trafficked location visible from the entrance. When the main entrance fronts the sidewalk, the installer must apply for an encroachment permit from the City to install the bicycle parking in the public right-of-way. The main building entrance excludes garage entrances, trash room entrances, and other building entrances that are not publicly accessible. (J) If required bicycle parking is not visible from the street or main building entrance, a sign must be posted at the main building entrance indicating the location of the bicycle parking. (e) Minimum Number of Required Bicycle Parking Spaces. The rules for calculating the minimum number of bicycle parking spaces are: (1) If after calculating the number of required bicycle parking spaces a quotient is obtained containing a fraction of one-half or more, an additional space shall be required; if such fraction is less than one-half it may be disregarded. (2) When the bicycle parking requirement is based on number of employees or number of students, the number of spaces shall be based on the number of working persons on the lot during the largest shift of the peak season or the highest expected student capacity. If the Zoning Administrator determines that this number is difficult to verify for a specific facility, then the number of required long-term bicycle parking spaces shall be a minimum of two (2) spaces or five (5) percent of the amount of required automobile spaces for the proposed facility, whichever is greater. (3) When the bicycle parking requirement is based on number of seats, in the case of pews or similar facilities each 18 inches shall be counted as one seat. (4) The calculation of short-term bicycle parking may include existing racks that are in the public right-of-way and are within 100 feet of the main entrance. (f) Bicycle Parking Rates. Required bicycle parking rates vary depending on whether the associated land use is located within or outside the Downtown Area as shown below:  (1) Downtown Area. (A) Minimum Parking Requirements. Where a parcel of real property is located within the Downtown Area, new projects to be located on said parcel shall meet the bicycle parking requirements as follows: (2) Outside Downtown Area. (A) Minimum Parking Requirements. For the following uses on property located outside the Downtown Area, bicycle parking stalls shall be provided as listed below. Bicycle parking stalls required on an employee basis shall be based on the maximum number of employees on duty, or residing, or both, on the premises at any one (1) time."
    },
    {
      "heading": "27.64.265 COMPACT CAR STALLS PERMISSIBLE.",
      "id": "/us/ca/cities/san-mateo/code/27.64.265",
      "text": "Compact car stalls meeting all standards set forth in this chapter and in the Standard Drawings and Specifications may be permitted as follows: (1) Where the number of required spaces is from 10 to 100, 30% of such spaces may be provided pursuant to compact car standards. (2) Where the number of required spaces is more than 100, 40% of such spaces may be provided pursuant to compact car standards. When computations under this section result in a fractional allowance of more than 0.75 compact spaces, one (1) additional such space may be provided."
    },
    {
      "heading": "27.64.267 RECREATIONAL VEHICLE STORAGE FACILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.267",
      "text": "Recreational vehicle storage facilities may be permitted as a special use subject to the following conditions: (a) Habitation Prohibited. Habitation of any kind shall not be permitted in stored vehicles. (b) Surfacing. Vehicle storage areas shall be improved with a compacted base of not less than four (4) inches thick and surfaced with a plant mix asphalt, concrete surface, or other surfacing acceptable to the Director of Public Works. (c) Vertical Clearance. Recreational vehicle storage facilities shall provide a vertical clearance of not less than 14 feet in all storage areas. (d) Standard Stall Sizes. Stall sizes for recreational vehicles shall be not less than nine (9) feet by 20 feet, 10 feet by 25 feet, and 10 feet by 30 feet. A mix of the stall sizes is desirable with reservation of larger stalls for larger vehicles. (e) Sight Distance. To maintain visibility into the interior of the facility, spaces closest to the periphery of the facility shall be occupied by recreational vehicles that do not exceed seven (7) feet in height or a height equal to the height of the fence, whichever is greater. Taller vehicles shall be parked in the center of the facility. (f) Sewage and Waste Facilities. Recreational vehicle storage lots containing 25 or more spaces shall provide and properly maintain facilities for the collection and disposal or treatment and disposal of sewage and other waste. The design and maintenance plan for such facilities shall be subject to approval of the Department of Public Works. (g) Lighting. The storage lot shall be illuminated at night so as to permit proper police surveillance. All lighting shall be directed away from adjoining properties and shall be adequate to meet the approval of the Police Department. (h) Security System. Facilities shall provide for security in a manner which meets the approval of the Police Department. (i) Fencing and Screening. All recreational vehicle storage spaces shall be securely enclosed and effectively screened on each side by a six (6) foot solid wall or solid fence, or densely planted shrub mass of a species whose height can be maintained between six (6) feet and eight (8) feet. Such required enclosure and screening shall conform with the sight distance requirements per SMMC Chapter 27.84 and with the front and side yard setback requirements of the district in which the lot is located, and shall meet the approval of the Police Department. (j) Transitional Yards and Buffers. Where a zoning district containing a recreational vehicle storage facility adjoins a residential district, a landscaped transitional yard of at least 15 feet shall be provided on site to screen the facility. Where this occurs adjacent to public rights-of-way, the landscaped transitional yard shall be on the right-of-way side of any fences or walls. Trees shall be a major element of the landscaped transitional yard."
    },
    {
      "heading": "27.64.269 VALET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.64.269",
      "text": "Commercial uses may provide valet parking to satisfy the parking requirements of this chapter as follows: (1) Special Use Permit. The provision of valet parking to meet this chapter's parking requirements may be authorized by the Planning Commission upon application for a special use permit according to the procedure set forth in Title 27. (2) Number of Spaces. Valet parking may be allowed for a project when the total number of required off-street parking spaces for the building or use is at least 50, and at least half of the total number of required spaces will be provided in a self-parking configuration either on-site or off-site in full compliance with the regulations of this chapter. (3) Design. The design of valet parking facilities need not conform to the regulations contained herein for self-parking facilities; provided, however, that such design meets with the approval of the Planning Commission. (4) Valet Parking System. In addition to the required drawings, the applicant shall submit a plan describing in detail the proposed number of attendants, hours of valet parking service operations, fees charged to patrons, and such other pertinent information as may be required from time to time by the Commission to enable it to determine the practicability of the valet parking proposal. (5) Discontinuance of Valet Parking. When an approved valet parking system provided to meet the requirements of this chapter is discontinued, intensity of the use formerly served by such parking shall be immediately reduced to the extent necessary to bring the use into full conformance with the parking requirements of this chapter."
    },
    {
      "heading": "27.64.270 OTHER USES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.270",
      "text": "For uses not listed heretofore in the schedules of parking requirements, parking spaces shall be provided on the same basis as required for the most similar listed use, or as determined by the Zoning Administrator."
    },
    {
      "heading": "27.64.310 LOCATION.",
      "id": "/us/ca/cities/san-mateo/code/27.64.310",
      "text": "Off-street loading facilities shall be located as follows: (a) All required loading berths shall be located on the same parcel as the use served. No loading berth for vehicles over two (2) ton capacity shall be closer than 50 feet to any property in a residence district unless completely enclosed by building walls, or a uniformly solid fence or wall, or any combination thereof, not less than six (6) feet in height. No permitted or required loading berth shall be located within 25 feet of the nearest point of intersection of any two (2) streets. (b) Freight-handling doors and facilities shall be oriented towards legal off-street loading berths and not towards street or curb parking. Freight-handling docks and loading areas shall not obstruct the use of aisles, drives and sidewalks."
    },
    {
      "heading": "27.64.320 SIZE.",
      "id": "/us/ca/cities/san-mateo/code/27.64.320",
      "text": "Loading stalls shall be of a size and number consistent with loading demands on an average business day under the intended use, but in no case shall they be less than the requirements of this chapter. Unless otherwise specified, a required loading berth shall be at least 10 feet in width by at least 25 feet in length, exclusive of aisle and maneuvering space, and shall have a vertical clearance of at least 14 feet. Where larger trucks will likely deliver to the proposed use, the loading berth, aisles, driveways, turnaround and overhead clearances shall be appropriately increased."
    },
    {
      "heading": "27.64.330 ACCESS.",
      "id": "/us/ca/cities/san-mateo/code/27.64.330",
      "text": "Each required off-street loading berth shall be designed with appropriate means of vehicular access to a street or alley in a manner which will least interfere with traffic movements and shall be designed to preclude backing out onto a public right-of-way."
    },
    {
      "heading": "27.64.340 SURFACING.",
      "id": "/us/ca/cities/san-mateo/code/27.64.340",
      "text": "All open off-street loading berths shall be improved with a compacted base, not less than five (5) inches thick, surfaces with not less than three (3) inches of plant mix asphalt, concrete or some comparable material approved by the Director of Public Works."
    },
    {
      "heading": "27.64.350 REPAIR—SERVICE.",
      "id": "/us/ca/cities/san-mateo/code/27.64.350",
      "text": "No motor vehicle repair work or service of any kind shall be permitted in conjunction with loading facilities provided in any residence or commercial district."
    },
    {
      "heading": "27.64.360 USE FOR OFF-STREET PARKING REQUIREMENT PROHIBITED.",
      "id": "/us/ca/cities/san-mateo/code/27.64.360",
      "text": "Space allocated to any off-street loading berth shall not, while so allocated, be used to satisfy the space requirements for any off-street parking facilities or portions thereof."
    },
    {
      "heading": "27.64.370 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.370",
      "text": "For special uses other than prescribed for hereinafter, loading berths adequate in number and size to serve such use, as determined by the Zoning Administrator, shall be provided."
    },
    {
      "heading": "27.64.380 RECEIVING FACILITIES.",
      "id": "/us/ca/cities/san-mateo/code/27.64.380",
      "text": "Uses for which off-street loading facilities are required herein but which are located in buildings of less floor area than the minimum prescribed for such required facilities shall be provided with adequate receiving facilities off any adjacent alley, service drive or open space on the same lot which is accessible by motor vehicle."
    },
    {
      "heading": "27.64.390 Schedule of Loading Requirements.",
      "id": "/us/ca/cities/san-mateo/code/27.64.390",
      "text": "All planning applications shall include a description of the means by which loading activities for the intended use are to be accommodated. For the uses listed in the following table, off-street loading berths shall be provided on the basis of number of residential units or gross floor area of building or portions thereof devoted to such uses in the amounts shown herein. Off-street loading berths as prescribed below shall be accessible from a public alley, driveway easement, or from an adjacent off-street parking area. The requirements for off-street loading berths may be modified by one of the following means: (a) Approval of a site plan and architectural review (SPAR) by the Zoning Administrator, based on the following findings: (1) Adequate on-street parking is available along a parcel frontage to accommodate a loading berth; (2) The on-street parking intended for temporary loading purposes is located at least 50 feet from any intersections, and provides convenient access to building entrances; and (3) The street width is adequate to accommodate loading vehicles without impeding use of the sidewalk or local traffic circulation or otherwise be detrimental to public safety; or (b) Approval of a variance application in accordance with Chapter 27.78."
    }
  ],
  "Chapter 27.65 AMUSEMENT ARCADES AND MACHINES": [
    {
      "heading": "27.65.001 INTENT.",
      "id": "/us/ca/cities/san-mateo/code/27.65.001",
      "text": "The intent of this chapter is to regulate the location of all forms of amusement machines including but not limited to electronic, electrical, mechanical, games of skill or any combination thereof, such as video games, pin ball, computer games, et cetera."
    },
    {
      "heading": "27.65.010 AMUSEMENT MACHINES.",
      "id": "/us/ca/cities/san-mateo/code/27.65.010",
      "text": "\"Amusement machine\" is any device, game or contrivance, including, but not limited to pin ball machines, video games, computer games and electronic games, for which a charge or payment is received for the privilege of playing, using or operating the same and which, as the result of such use, operation or playing does not entitle the person using, operating or playing such device, game or contrivance to receive the same return in market value in the form of tangible merchandise each time such device, game or contrivance is used, operated or played."
    },
    {
      "heading": "27.65.020 ARCADES.",
      "id": "/us/ca/cities/san-mateo/code/27.65.020",
      "text": "\"Arcade\" is defined as any business or establishment which has located on its premises five or more amusement machines which are kept thereon for the purpose of being played, operated or used by the patrons of the arcade on a prepaid basis or for money or tokens deposited in the amusement machine played, operated or used. Arcade is also defined as any premises wherein not less than twenty-five percent of the public floor area is devoted to amusement machines whether or not said amusement machines constitute the primary use or accessory use of the premises."
    },
    {
      "heading": "27.65.030 ARCADE: PERMITTED IN COMMERCIAL ZONES.",
      "id": "/us/ca/cities/san-mateo/code/27.65.030",
      "text": "Arcades may be permitted in any commercial zone including the CBD District. (a) Unless a special use permit is first obtained from the City planning commission, no arcade shall be maintained or operated within fifty feet from the property line of any residential zone."
    },
    {
      "heading": "27.65.040 LIMITATION ON LOCATION OF ARCADES AND AMUSEMENT MACHINES.",
      "id": "/us/ca/cities/san-mateo/code/27.65.040",
      "text": "(a) Unless specific approval is first obtained from the City planning commission, no arcade shall be maintained or operated within fifty feet from the property line of any residential zone. (b) No amusement machine accessible for use by minors shall be maintained, operated, conducted or used, nor kept for such purposes, in or on the premises of any establishment whose primary business is the sale of alcoholic beverages. This subsection shall not prohibit the operation of amusement machines in a bona fide establishment with an on-sale liquor license or restaurants which are licensed to sell alcoholic beverages. (c) No amusement machine as herein defined shall be maintained, operated, conducted or used, nor kept for such purposes, within any place which is closer than three hundred feet from any public or private school which conducts classes for any of the grades from kindergarten through twelfth grade."
    }
  ],
  "Chapter 27.66 HISTORIC PRESERVATION": [
    {
      "heading": "27.66.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.66.010",
      "text": "(a) Objectives. It is found that the protection, enhancement, perpetuation and use of historic structures within the City of San Mateo are of economic, cultural, and aesthetic benefit to the community. It is further found that the economic, cultural and aesthetic standing of the City will be enhanced by respecting the heritage of its historic structures and the downtown historic district. The purposes of this chapter are as follows: (1) Designate, preserve, protect, enhance, and perpetuate the City's historic structures and the downtown historic district; (2) Foster public awareness and appreciation of the City's past; (3) Stabilize and improve the economic value of structures and properties within the City and the downtown historic district; (4) Develop and maintain appropriate settings for historic structures; (5) Enhance the visual and aesthetic character, diversity and interest of the City; and (6) Establish requirements to insure the preservation and maintenance of the City's historic structures and the downtown historic district."
    },
    {
      "heading": "27.66.020 APPLICABILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.66.020",
      "text": "(a) Historic Buildings and Downtown Historic District. The provisions of this chapter shall apply to all individually eligible buildings in the City, all individually eligible and contributor buildings within the Downtown Specific Plan area, and all structures located in the Downtown Historic District, as adopted by resolution of the City Council. (b) The City Council by resolution may add to the provisions of this chapter any building which it finds meets the criteria of contributing to the historic importance of downtown and the City. Such an action shall be based on National Register of Historic Places and California Register of Historical Resources criteria and documented in a form consistent with the City of San Mateo Historic Building Survey. (c) Individually Eligible and Contributor Buildings. For the purposes of this chapter, the terms \"individually eligible building\" shall mean those buildings as identified in the City of San Mateo General Plan, buildings which are on the National Register of Historic Places (NRHP) or California Register of Historical Resources (CRHP), or buildings determined to be individually eligible for listing on the NRHP or CRHP through documentation contained in a historic resources report. \"Contributor building\" shall mean those buildings identified as such and located within the Downtown Historic District as adopted by resolution of the City Council and identified in the City of San Mateo General Plan. (d) For the purposes of this chapter, the terms \"individually eligible building\" and \"contributor building\" and \"Downtown Historic District\" shall mean those buildings and district identified as such by resolution of the City Council, identified in the City of San Mateo Downtown Specific Plan, or as determined to be listed or individually eligible for listing on the NRHP or CRHP through documentation contained in a historic resources report."
    },
    {
      "heading": "27.66.030 REVIEW REQUIRED.",
      "id": "/us/ca/cities/san-mateo/code/27.66.030",
      "text": "(a) Individually Eligible Buildings. No building permit for an exterior facade modification, exterior alteration, or building addition involving an individually eligible building shall be issued until a planning application for Site Plan and Architectural Review has been approved in accordance with the provisions of Chapter 27.08 and Section 27.06.010 of the Zoning Code. (b) Contributor Buildings. Unless otherwise required by this code, minor facade modifications, in accordance with Section 27.08.031, which conform to the adopted Downtown Retail Core and Downtown Historic District Design Guidelines, shall be exempt from the requirements for a Site Plan and Architectural Review. However, the Zoning Administrator may require submittal and approval of a Site Plan and Architectural Review application in cases involving facade modifications which may adversely affect the exterior architectural characteristics or historic or aesthetic value of the historic structure, its site or surroundings. (c) In all cases involving alteration of significant historical building details, building modifications or new buildings which may affect the integrity of the historic district, or construction which may affect individually eligible or contributor buildings, the Zoning Administrator may require an independent analysis by an architectural historian of the project's impact on downtown historic resources. The incorporation of the report's findings and recommendations may be incorporated as conditions of approval."
    },
    {
      "heading": "27.66.040 CONFORMANCE WITH STANDARDS AND GUIDELINES.",
      "id": "/us/ca/cities/san-mateo/code/27.66.040",
      "text": "(a) City-wide. All exterior modifications of individually eligible and contributor buildings (e.g., exterior building additions and alterations) shall conform with the Secretary of Interior's Standards for Rehabilitation and Guidelines for Rehabilitating Historic Structures, 1990 Edition. (b) Downtown. In addition to the requirements of (a) above, all exterior modifications of individually eligible and contributor buildings and new buildings in the Downtown Retail Core subarea of the Downtown Specific Plan (e.g., exterior building additions and alterations) shall conform with the Downtown Retail Core and the Downtown Historic District Design Guidelines."
    },
    {
      "heading": "27.66.050 MAINTENANCE.",
      "id": "/us/ca/cities/san-mateo/code/27.66.050",
      "text": "(a) Routine Maintenance. Nothing in this chapter shall be construed to prevent routine building maintenance and repair which does not involve a change in design, material or appearance and is consistent with the standards and guidelines in Section 27.66.040. (b) The owner, lessee or other person legally in possession of a building shall comply with all applicable codes, laws and regulations governing the maintenance of property. It is the intent of this section to preserve from deliberate or inadvertent neglect the exterior features of such buildings, and of the interior portions of such buildings which are necessary to prevent deterioration and decay of the exterior."
    },
    {
      "heading": "27.66.060 DEMOLITION.",
      "id": "/us/ca/cities/san-mateo/code/27.66.060",
      "text": "(a) For the purposes of this section, demolition shall mean the wrecking, destroying or destruction of an individually eligible or contributor building or a major portion of such structure, including exterior architectural features. (b) Individually eligible buildings. Individually eligible buildings may be demolished in whole or in part only upon a finding by the City Council that applicable health and safety requirements cannot be feasibly met unless the building is demolished. (c) Any request for demolition of an individually eligible or contributor building shall be processed as a discretionary planning application as described in Chapter 27.08. As part of this planning application, a Historic Building Demolition Permit, a report by a civil or structural engineer or architect licensed by the State of California shall be submitted identifying the general condition of the building, all health and safety code deficiencies, corrective measures needed to alleviate these deficiencies, and the cost of such corrective measures. (d) Other regulations. All demolitions shall conform with the provisions of Chapter 23.10 Earthquake Hazard Reduction in Existing Buildings and Section 23.06.035 Demolition Permits-Conditions."
    }
  ],
  "Chapter 27.67 OPEN AIR VENDORS": [
    {
      "heading": "27.67.010 INTENT.",
      "id": "/us/ca/cities/san-mateo/code/27.67.010",
      "text": "The intent of this chapter is to regulate open air vendors selling prepared food, fresh cut flowers or plants."
    },
    {
      "heading": "27.67.020 OPEN AIR VENDORS.",
      "id": "/us/ca/cities/san-mateo/code/27.67.020",
      "text": "\"Open Air Vendors\" means persons who sell prepared food, fresh cut flowers or plants from a stand or non-motorized, non-stationary cart or pushcart on private property."
    },
    {
      "heading": "27.67.030 OPEN AIR VENDOR: SPECIAL PERMIT REQUIRED.",
      "id": "/us/ca/cities/san-mateo/code/27.67.030",
      "text": "Open air vendors may be permitted on executive or commercial (including the Central Business District) zoned private property and specific locations on said property subject to the approval of a Special Permit by the Planning Commission."
    },
    {
      "heading": "27.67.040 PROPERTY OWNER'S CONSENT.",
      "id": "/us/ca/cities/san-mateo/code/27.67.040",
      "text": "The property owner(s) written consent shall be filed with an application for a special use permit. The property owner shall be ultimately responsible for the manner in which open air vending is operated on his or her /her property."
    },
    {
      "heading": "27.67.050 DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.67.050",
      "text": "Vacant unimproved property shall not be considered for open air vending. Open air vendors may be permitted on improved private property when: (a) There is an existing operating primary use on-site. Leases for open air vending space shall run concurrent with the primary lease. (b) The open air vendor is considered to be an incidental use on the property. (c) The space for the vendor does not occupy required off-street parking spaces. (d) The space for the vendor is convenient to existing pedestrian movement and does not interfere with vehicular circulation and parking. (e) Sturdy and rigid refuse containers which are animal proof and a litter control plan are provided."
    },
    {
      "heading": "27.67.060 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.67.060",
      "text": "The following conditions shall apply to all open air vendors as defined by this chapter: (a) Open air vendors shall be limited to the sale of flowers, plants or food for immediate consumption such as hot dogs, sandwiches, ice cream and non-alcoholic beverages. (b) The hours of operation shall be established on a case-by-case basis by the Planning Commission but in no case shall they exceed the hours of operation for the primary use on subject site. (c) There shall be no vending from a truck, van, automobile, or other motorized vehicle. (d) A clearance by the County Health Officer shall be on file with the City as part of the application, when applicable. (e) The maximum overall size of the stand or non-motorized non-stationary cart or pushcart, hereafter referred to as \"conveyance\" shall be established on a case-by-case basis by the Planning Commission. (f) Signs shall be limited to non-electrical signs that are permanently affixed to the vendor's conveyance. The total sign square footage shall not exceed 6 (six) square feet. (g) Items for sale shall be confined to the vendor's conveyance. However, areas immediately adjacent to the vendor's conveyance may be used for sales purposes when it can be demonstrated that the location will not impede pedestrian or vehicular circulation. (h) Noise generating devices, such as, but not limited to horns, bells, loudspeakers or amplifiers, shall not be used."
    },
    {
      "heading": "27.67.070 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.67.070",
      "text": "Off-street parking and loading is not required for open air vendors."
    }
  ],
  "Chapter 27.68 MAINTENANCE OF PROJECT SITE": [
    {
      "heading": "27.68.010 FINDINGS AND INTENT.",
      "id": "/us/ca/cities/san-mateo/code/27.68.010",
      "text": "The Council finds that the community's standard of care and maintenance of real property in the City is significantly higher than the standard established by Titles 7 and 10 of this code for creation of a public nuisance. It is, therefore, a matter of public concern when a site for an approved development is allowed to deteriorate for a period of time before construction begins even if it does not become a public nuisance under this code. This chapter is intended to provide the enforcement power to compel and the incentive otherwise lacking for the owner and the project developer to maintain the property at a level consistent with the neighboring properties and its condition at the time of the project approval. These measures are needed to prevent unnecessary loss of tax revenues and park in-lieu fees caused by the depreciating effect of the site's condition, to protect the health, safety, and general welfare of the City, and to safeguard the aesthetic standards of the community."
    },
    {
      "heading": "27.68.020 REQUIREMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.68.020",
      "text": "(a) Prior to approval of a project pursuant to this title, any violations of Federal, State, or local laws existing on the site shall be corrected so that all structures are habitable and free from all public nuisances. If the property owner or applicant believes that it is not feasible to restore existing structures to a habitable condition, the owner or applicant may present evidence of infeasibility and request that a demolition permit be issued. The Planning Commission shall review the request as part of the planning application, and may grant the request if it makes all the findings in Section 23.06.035(f)(1)(F). The decision of the Planning Commission may be further appealed to the City Council pursuant to Section 27.08.090. (b) After approval of a project pursuant to this title and until a building or demolition permit is issued and construction or demolition for the project has begun, the owner of the project site and the owner of the development rights for the project shall maintain the structures and the project site so that they are habitable and free of all public nuisances, and shall prevent visible deterioration of the grounds or structures on the site from their condition and appearance at the time of the project approval."
    },
    {
      "heading": "27.68.030 REVIEW FOR COMPLIANCE.",
      "id": "/us/ca/cities/san-mateo/code/27.68.030",
      "text": "(a) At the written request of any person, the Community Relations Commission shall conduct a compliance review hearing to determine whether the site of a project that has been approved but not yet begun has been maintained in accordance with this chapter. This review shall be conducted in the same manner as all other reviews by the Commission under this title, except that notice to the owners of property within 300 feet of the site as required by this title shall also be given 10 days before the hearing date. (b) In making its determination, the Community Relations Commission may rely on dated photographs showing the site before, but not more than six months before, the project was approved and any time after the approval. In the absence of or in addition to this photographic evidence, the Commission may base its decision on the testimony of any two eyewitnesses giving evidence of deterioration or on a written report by the landscape resources, building, or bureau of fire prevention and life safety divisions or the health official based on on-site inspections by the reporting official before and after approval of the project. The Commission shall permit testimony from the public at the hearing. (c) If a public nuisance has been determined to exist on the site concerned pursuant to Chapter 10.08 before the date of the review hearing under this chapter, that finding shall be binding and conclusive on review under this chapter. If it was determined pursuant to Chapter 10.08 that no public nuisance existed on the site, that decision shall have no force or effect on the review under this chapter. (d) The determination of the Community Relations Commission under this chapter shall be subject to appeal as provided by Chapter 27.08."
    },
    {
      "heading": "27.68.040 PENALTIES AND REMEDIES.",
      "id": "/us/ca/cities/san-mateo/code/27.68.040",
      "text": "(a) It is unlawful for an owner of the site or owners of development rights on a site to violate any provisions of this chapter. (b) Any person or entity who violates the provisions of this chapter shall be liable civilly in a sum of $5,000.00 per parcel. (c) The remedies in this section are cumulative and in addition to any and all remedies available under law or equity."
    },
    {
      "heading": "27.68.050 MAINTENANCE OF YARDS, COURTS, AND OTHER OPEN SPACES.",
      "id": "/us/ca/cities/san-mateo/code/27.68.050",
      "text": "The maintenance of yards, courts, and other open space and minimum lot area legally required for a building shall be a continuing obligation of the owner of such building or of the property on which it is located, as long as the building is in existence. No legally required yards, courts, other open space or minimum lot area allocated to any building shall, by virtue of change of ownership or for any other reason, be used to satisfy yard, court, other open space, or minimum lot area requirements for any other building."
    }
  ],
  "Chapter 27.69 RECYCLING FACILITIES": [
    {
      "heading": "27.69.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.69.010",
      "text": "The purpose of the Chapter is to set forth procedures to permit and regulate the establishment of recycling facilities subject to certain standards and conditions."
    },
    {
      "heading": "27.69.020 DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.69.020",
      "text": "The following minimum development standards shall apply to all recycling facilities and reverse vending machines in the City. For the purpose of this section, the term \"facility\" shall mean all recycling centers, reverse vending machines, and bulk reverse vending machines. (a) All facilities shall be constructed of durable waterproof and rustproof material. Such containers shall be secured from unauthorized entry. (b) All facilities shall be maintained in a clean or litter free condition on a daily basis. (c) All facilities shall be clearly marked to identify the type of material which may be deposited. The facility shall be clearly marked to identify the name and telephone number of the facility operator, hours of operation, and a notice stating that no materials shall be left outside the recycling container. (d) All storage of material shall take place within the facility; no outdoor storage of material is permitted. (e) No facility shall occupy required parking spaces, landscape areas, or transition yards nor obstruct pedestrian, vehicular, or emergency vehicle access. (f) Containers for the 24-hour donation of materials shall be at least 100 feet away from any abutting residential zoned property. (g) Hours of operation for attended facilities shall be limited to 8 a.m. to 9 p.m. (h) There shall be no more than one (1) recycling center and three (3) reverse vending machines on one site. (i) All facilities shall be located on sites with permanent, operating, legally established businesses. (j) Design and colors of the center shall be compatible with other businesses on the site. Improvements may be required to ensure compatibility, including but not limited to landscaping, screening, trailer skirting, and parking lot improvements."
    },
    {
      "heading": "27.69.030 SIGNAGE.",
      "id": "/us/ca/cities/san-mateo/code/27.69.030",
      "text": "(a) Reverse Vending Machines—Signage shall not exceed four (4) square feet per machine (not including operating instructions) and shall be mounted flat on the side of the machine. (b) Recycling Facilities—Signage shall be limited to sixteen (16) square feet (not including operating instructions)."
    },
    {
      "heading": "27.69.040 OFF-STREET PARKING.",
      "id": "/us/ca/cities/san-mateo/code/27.69.040",
      "text": "Reverse vending machines shall not increase the off-street parking requirement of the site's principal use. Recycling centers shall provide one additional off-street parking space for each attendant and drop-off area for unloading of materials."
    }
  ],
  "Chapter 27.70 ACCESSORY BUILDINGS AND STRUCTURES IN REQUIRED YARDS": [
    {
      "heading": "27.70.010 ACCESSORY BUILDINGS.",
      "id": "/us/ca/cities/san-mateo/code/27.70.010",
      "text": "(a) Location of Detached Accessory Buildings. A detached accessory building located within the rear one-third of a parcel is exempt from the requirements for interior side and rear yards, provided such structure is separated from the principal building by an area not less than four (4) feet in width that is open to the sky. (b) Maximum coverage of required rear yards. Accessory buildings shall not occupy more than 50% of a required rear yard. (c) Maximum height of accessory structures in required yards. Accessory structures located in required yards pursuant to subsection (a) shall not exceed the following height limits: (d) Habitable floor limitation. In R1 Districts, accessory structures located in required yards pursuant to subsection (a) shall be limited to one habitable floor on the ground level. Habitable floor for the purposes of this subsection shall mean that served by permanent access and containing windows and/or plumbing fixtures, but shall exclude basements."
    },
    {
      "heading": "27.70.020 STRUCTURES OR BUILDING PROJECTIONS IN REQUIRED YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.70.020",
      "text": "(a) R1 Districts. In R1 Districts, Section 27.18.100 shall govern structures or building projections in required yards. (b) All other districts. For all other districts, the following structures, building projections or features shall be permitted in all yards: (1) Overhanging eaves and gutters projecting a maximum of three (3) feet or fifty percent (50%) of the required yard width, whichever is less; (2) Awnings, canopies and covered patios; (3) Greenhouse or oriel bay windows projecting three (3) feet or less into a required yard, provided that the outside face of the projection shall be at least three (3) feet from the property line; (4) Chimneys projecting two (2) feet or less into a required yard provided that the outside face of the chimney shall be at least three (3) feet from the property line; (5) Arbors and trellises having a maximum height of eight (8) feet; (6) Flag poles, garden ornaments and play equipment; (7) Fences, subject to provisions of Chapter 27.84 of this title; (8) Basements which are completely below grade; (9) Steps which are necessary to provide access to the first living level of a permitted building or to a parcel from a street or alley; (10) Open swimming pools and spas, subject to setbacks from property lines established in Section 23.44.030 of this title. (c) Front yard projections. For districts other than R1, the following structures or building projections shall be permitted in front yards: (1) Balconies or decks projecting six (6) feet or less into the required yard; (2) Porte cochere or similar pedestrian entry feature in multi-family or commercial developments which are less than six hundred (600) square feet in total area and have a width less than twenty (20) percent of the property street frontage. (d) Rear yard projections. For districts other than R1, the following structures, building projections or features shall be permitted in rear yards: (1) Accessory structures subject to provisions of Section 27.70.010 of this title; (2) Open parking spaces; (3) Balconies or decks projecting six (feet) or less into the required yard; (e) Interior side yard projections. For districts other than R1, the following structures, building projections or features shall be permitted in interior side yards: (1) Accessory structures subject to provisions of Section 27.70.010 of this title; (f) Street side yard projections. For districts other than R1, the following structures, building projections or features shall be permitted in street side yards: (1) Balconies or decks projecting not more than three (3) feet, provided that the distance between the projection and the street property line shall be at least 7.5 feet. (2) Porte cochere or similar pedestrian entry feature in multi-family or commercial developments which are less than six hundred (600) square feet in total area and have a width less than twenty (20) percent of the property street frontage. (f) In all districts, covered pools are not allowed in required yards. "
    }
  ],
  "Chapter 27.71 LANDSCAPE FOR PLANNING APPLICATIONS": [
    {
      "heading": "27.71.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.71.010",
      "text": "The purpose of this chapter is to enhance the quality of life in San Mateo by the provision for appropriate design of landscaping and through the preservation of existing trees. Landscaping shall be a major component of all site design in order to create a city that has a strong landscaped character. The intent is that individual neighborhood character be developed and maintained, architecture be softened by plant materials where appropriate, conflicting uses be buffered, parking areas be screened, comfortable outdoor living and walking spaces be created, air pollution be mitigated and future developments be made water efficient."
    },
    {
      "heading": "27.71.020 Scope.",
      "id": "/us/ca/cities/san-mateo/code/27.71.020",
      "text": "(a) This chapter shall apply as a minimum for all projects requiring approval of a planning application pursuant to Section 27.08.010, except for single-family dwelling design review applications. Landscaping not subject to this chapter shall be governed by the provisions of Chapter 13.40. The Zoning Administrator may determine that minor additions or changes to existing property are not reasonably related to the purpose of this chapter and may be exempt from the requirements of this chapter."
    },
    {
      "heading": "27.71.030 GENERAL OBJECTIVES.",
      "id": "/us/ca/cities/san-mateo/code/27.71.030",
      "text": "(a) Required Landscaping. All required front and street side yards shall be landscaped, except for necessary driveways and walkways. In all other areas landscaping shall be required except for necessary circulation areas, paved outdoor living areas or water features. (b) Buffering and Screening. Plantings shall be provided to buffer residential uses from commercial or industrial uses. Plantings shall also be provided to screen service and storage areas, parking lots or unsightly areas. Plantings shall be used where appropriate to control noise, wind, climate and ensure privacy. (c) Outdoor Living Areas. Landscaping shall be arranged so as to provide usable outdoor living areas where appropriate. Plant materials and architectural features should be used to control noise, sun and wind and provide adequate privacy. (d) Composition of Required Landscaping. All required landscaping shall include the planting and maintenance of some combination of trees, groundcover, shrubs, vines, annuals and lawns. In addition, the combination or design may include natural or structural features, including, but not limited to, fountains, reflecting pools, artwork, screens, walls, and fences. (e) Security. Landscaping shall be installed and maintained to provide aesthetic quality while promoting building security. (f) Minimum Requirements. The provisions contained in this chapter are intended to be a minimum standard. Compatibility with other projects and compliance with required findings and adopted goals and policies of the City shall be evaluated through the planning application process."
    },
    {
      "heading": "27.71.040 Definitions.",
      "id": "/us/ca/cities/san-mateo/code/27.71.040",
      "text": "The following definitions shall apply to this chapter: (a) \"Existing Trees\" means all existing trees over six inches in trunk diameter (measured at 54 inches from natural grade) on the subject property and any Protected Trees on the subject property or any property within 30 feet of the proposed Construction Activity, as outlined in Chapter 13.40. (b) \"Groundcover\" means low growing live perennial vegetation, other than turf, of a species which is sold as a groundcover or shrub by licensed nurserymen. (c) A \"heritage tree\" is as defined in Chapter 13.40. (d) \"Landscape\" or \"landscaped area\" means an area that consists of living plantings. (e) \"Landscape unit (LU)\" means the unit of measurement for trees which indicates the worth of each relative to one another and towards satisfying City requirements. (f) \"Natural landscaping\" means an area consisting of uncultivated native plant growth and other features of natural terrain such as rock outcroppings, streams or other areas covered by water. (g) \"Plantings\" means annuals, groundcover, turf grass, shrubs or trees. (h) \"Protected Tree\" means a Heritage Tree or Street Tree as defined in Chapter 13.40 or a tree designated as protected as part of an approved Planning Application that is subject to this Chapter. (i) \"Project Arborist\" means an ISA Certified Arborist designated to evaluate the potential impacts of Construction Activity on Protected Trees, write specifications for tree preservation, oversee Construction Activity within the Dripline of Protected Trees and other necessary activities as determined by the City Arborist. (j) \"Shrubs\" means live perennial vegetation, greater than an average height of two (2) feet and maintained below twelve (12) feet in height. Vines shall be considered shrubs. (k) \"Street Tree\" means any woody perennial plant having a single main axis or stem capable of achieving ten (10) feet or more in height, growing along or within public right of way or planted within public right of way or a designated planting easement. (l) \"Trees\" means a live self-supporting woody plant having at least one well defined stem or trunk and normally attaining a mature height and spread of at least twelve (12) feet, and having a trunk that may, at maturity, be kept clear of leaves and branches at least six (6) feet above grade. (m) \"Turfgrass\" means live vegetation of a species normally grown as turf by a nursery and which is maintained at a height of three inches or less."
    },
    {
      "heading": "27.71.050 MAINTENANCE.",
      "id": "/us/ca/cities/san-mateo/code/27.71.050",
      "text": "All landscape areas shall be maintained free of weeds, litter and debris. All plantings shall be maintained in a healthy growing condition and whenever necessary, replaced with equivalent plant materials to ensure continued conformance with approved plans."
    },
    {
      "heading": "27.71.060 PLANT ESTABLISHMENT PERIOD.",
      "id": "/us/ca/cities/san-mateo/code/27.71.060",
      "text": "A plant establishment period of three growing season months (March through October) shall be required for all landscape areas. At the completion of this period all plant materials shall be in a healthy condition and the landscaped area shall be maintained free of weeds, litter and debris. (a) For projects with less than 10,000 square feet of landscaped area, proof of a contract with a licensed landscape contractor to maintain the landscape for the plant establishment period shall be submitted. (b) For projects with greater than 10,000 square feet of landscape area and for all residential condominiums, financial securities shall be held by the City as required in Section 27.71.090 to ensure compliance with the plant establishment period."
    },
    {
      "heading": "27.71.070 Submittals Required for a Planning Application.",
      "id": "/us/ca/cities/san-mateo/code/27.71.070",
      "text": "(a) All landscape plans must be at a reasonable scale to indicate all types of improvements. All plans must contain sufficient information to ensure conformance with the requirements of this chapter and must include, but are not limited to, the following information: (1) North arrow and scale; (2) The name of the applicant/owner; (3) The name, address, and phone number of the person or firm responsible for the preparation of the plans and other required information; (4) The dates the plans are submitted and revised; (5) All existing and proposed buildings and other structures, paved areas, planted areas, power poles, fire hydrants, light standards, signs, fences, and other permanent features to be added and/or retained on the site; (6) All existing plant material to remain and to be removed, a tree evaluation schedule identifying Major Vegetation (as defined in Chapter 23.40) and all Protected Trees including trunk diameter, species, the condition of trees to be removed as determined by an arborist and the existing and proposed replacement Landscape Unit (LU) values; (7) All existing and proposed streets, sidewalks, curbs and gutters, railroad tracks, drainage ditches, and other public or semi-public improvements within and immediately adjacent to the site; (8) Contour lines, if the slopes are in excess of 10%; (9) Existing and proposed topographic elevations at sufficient locations, to clearly show the drainage pattern unless this information is provided on a grading plan or other documents in the planning application; (10) All property lines and easements; (11) Square footage of all planted area; (12) Species, sizes and location of all proposed plant material including the accurate driplines of all Protected Trees; (13) Soil tests as required by the discretion of the Zoning Administrator; and (14) A tree protection plan consistent with Chapter 13.40 and the Administrative Guidelines. (b) All projects with over 1,000 square feet of new or modified planting areas as required to meet the provisions of this chapter shall have all landscape plans and accompanying documents prepared or reviewed and found acceptable by a licensed landscape architect registered with the State of California."
    },
    {
      "heading": "27.71.080 Submittals Required for a Building Permit Application.",
      "id": "/us/ca/cities/san-mateo/code/27.71.080",
      "text": "(a) All of the required submittals for a planning application; (b) Type and depth of mulch indicated on the plan; (c) An irrigation plan accurately drawn to scale that indicates all components of the irrigation system including sprinklers and other outlets, valves, the backflow prevention device(s), controller(s), and piping; (d) All tree information required in Section 27.71.150 and Chapter 13.40; (e) For projects with less than 10,000 square feet of landscaped area, proof of a contract with a licensed landscape contractor to maintain the landscape area for the plant establishment period; (f) For projects with greater than 10,000 square feet of landscape area, financial securities as required in Section 27.71.090; and (g) Soil tests as required in Section 27.71.110."
    },
    {
      "heading": "27.71.090 REQUIREMENTS FOR USE OR ISSUANCE OF A CERTIFICATE OF OCCUPANCY.",
      "id": "/us/ca/cities/san-mateo/code/27.71.090",
      "text": "(a) Prior to use, final inspection, or the issuance of certificate of occupancy, all landscaping shall be installed in conformance with the approved plans. (b) Phased Projects. Incremental landscape installation may be permitted by the Zoning Administrator when building construction is phased. (c) Financial Security. Financial security shall be required for all projects with over 10,000 square feet of landscape area and for all residential condominiums. On smaller projects where adverse weather, drought conditions or project phasing prohibit the installation of landscaping, the Zoning Administrator may allow financial security to be submitted to the City in order to allow use or issuance of a certificate of occupancy. The security shall be in a form which is legally sufficient to ensure the preservation of trees and the installation of all approved landscape improvements. Financial security shall be returned to the applicant upon completion of the plant establishment period. The City shall be the beneficiary and the sole determinant of compliance and completion. A detailed cost estimate of all landscape improvements plus the value of any existing trees to remain, as determined in Section 27.71.150, shall be used to determine the amount of security."
    },
    {
      "heading": "27.71.100 LANDSCAPE COMPATIBILITY AND SOIL TESTING.",
      "id": "/us/ca/cities/san-mateo/code/27.71.100",
      "text": "The location and nature of all landscaping shall be compatible with the soil, amendments, existing plantings to remain and character of the landscaping in the vicinity. For projects with over 10,000 square feet of landscape area or in areas of questionable soils such as the foothills or areas of bay fill, soils testing shall be required. Testing shall be performed by a professional testing laboratory. Soil shall be amended according to test report recommendations."
    },
    {
      "heading": "27.71.110 Plant Coverage and Tree Sizes.",
      "id": "/us/ca/cities/san-mateo/code/27.71.110",
      "text": "(a) Allowed Bare Ground. Areas of bare ground or ground covered only by bark or rocks shall be allowed on-site only where required as part of an approved facility, such as a baseball diamond, vegetable garden, flowerbed, or similar use. (b) Allowed Natural Landscaping. Natural landscaping shall be allowed only in areas where it is compatible with the surrounding environment. (c) Minimum Tree Size. All required trees shall be a minimum size of 15-gallon container at time of installation, except for heritage tree replacements, which shall be replaced according to Chapter 13.40 and the Administrative Guidelines. (d) Plant Coverage. (1) Trees shall be planted at a minimum ratio of one per 400 square feet of required landscaped area. The ratio may include existing trees and required parking area trees. Public parks, golf courses, cemeteries, school recreation areas and public facilities need not comply with this ratio. (2) Groundcover and shrub massing areas shall be planted in a manner or at the spacings recommended by the American Association of Nurserymen, to uniformly cover the proposed groundcover areas within two years and the shrub areas within five years or a period optimum for the species. (e) Security Planting. The use of plant materials that promote building security is encouraged. A list of such materials may be obtained from the Planning Division. Perimeter landscaped areas should incorporate thorny plant materials to discourage persons from cutting through parking areas, trampling vegetation near ground floor windows, or climbing perimeter fences and walls."
    },
    {
      "heading": "27.71.120 Street Trees.",
      "id": "/us/ca/cities/san-mateo/code/27.71.120",
      "text": "(a) Tree Planting. (1) 24-inch box size or larger street trees shall be planted along public streets in accordance with the City Street Tree Master Plan. The City Arborist shall have the authority to recommend planting of fifteen (15) gallon street trees when: (A) Upon written request by the applicant; and (B) The fifteen (15) gallon size trees are the only ones available in stock, or (C) The quality of the fifteen (15) gallon size trees are superior to that available in 24-inch box size. (2) Trees shall be planted at a spacing not to exceed thirty (30) feet except to allow for utilities, street furnishings, driveways, or other features necessary to ensure public safety, as approved by the City Arborist. (b) Access Easement. Where a planning application requires a parcel or tentative map, an access easement shall be required if the street trees are to be located on private property and no such easement exists. However, it is recommended that even when a parcel or tentative map is not required or included, an easement be provided to the City for site access purposes in the event of an emergency or a hazardous situation."
    },
    {
      "heading": "27.71.130 PARKING AREAS.",
      "id": "/us/ca/cities/san-mateo/code/27.71.130",
      "text": "The following requirements shall apply to open parking areas containing five or more parking spaces. (a) Setbacks. Whenever a parking area is located adjacent to any residential use or zone and along all street frontages, a landscape strip shall be provided that is equal in width to five percent of the parking lot depth or six feet, whichever is greater. (b) Percentage of Parking Areas to be Landscaped. At least 10% of the open parking area shall be landscaped. The following shall be considered in computing the landscape area: (1) Parking area includes all paved surfaces devoted to on-site circulation and parking; (2) Only those landscaped areas within six feet of a parking stall or aisle shall apply towards meeting the 10% requirement; (3) Areas to be considered shall include planting areas and required curbing. (c) Screening. All open parking areas shall be effectively screened on each side adjoining or fronting on any property in a residential zone and along all street frontages. Screening of adjoining property shall be a minimum of four feet to a maximum of six feet in height. Screening along street frontages shall be at least two and one-half feet in height for at least 80% of its length. Screening shall be accomplished by a wall, fence, earth berm, densely planted shrub mass or any combination of the above. Where walls or fences are provided, they shall be located adjacent to the edge of the parking lots. Screening shall conform with the sight distance requirements contained in Chapter 27.84 of the San Mateo Municipal Code. (d) Parking Lot Islands. (1) All islands and small areas unused for parking or circulation shall be landscaped. The Zoning Administrator may determine that certain areas for reasons of size, aesthetics or circulation should not be landscaped and may approve paving in those areas. (2) Interior landscape islands, having a minimum dimension of five feet including curb, shall be provided after every 10 parking spaces in a row to provide for tree planting. (e) Required Trees. For each three parking spaces at least one tree shall be planted within the parking lot landscaped area in addition to any required street trees. Existing trees may be included in the required total. (f) Protection of Planting Areas. All planting areas shall be protected from common vehicular traffic. For parking lots containing five stalls or more, this requirement shall be met by a six-inch-high vertical concrete curb. For parking lots containing less than five stalls, this requirement may be met by a concrete wheel stop in front of each diagonal or perpendicular stall plus a minimum six-inch-high concrete curb in other areas or approved equal. No trees or shrubs shall be planted and sprinkler heads shall be kept below curb height within two feet six inches of any curb or wheel stops which front upon parking stalls or backup areas."
    },
    {
      "heading": "27.71.140 RIGHT-OF-WAY LANDSCAPING.",
      "id": "/us/ca/cities/san-mateo/code/27.71.140",
      "text": "The unpaved right-of-way area located between the public street and private property shall be landscaped in a manner compatible with the required landscaping on site. Such landscaping shall be permanently maintained by the property owner in conformance with the approved plans and so as not to create a safety hazard. Strips of public right-of-way located between the curb and sidewalks may not be paved but must likewise be landscaped. Long narrow strips of turfgrass such as traffic medians and areas between curbs and sidewalks are prohibited."
    },
    {
      "heading": "27.71.150 Preservation of Existing Trees.",
      "id": "/us/ca/cities/san-mateo/code/27.71.150",
      "text": "(a) Evaluation of Existing Trees. Trees over six (6) inches in trunk diameter, measured at 54 inches from natural grade and Protected Trees as defined in Chapter 13.40 shall be evaluated on the basis of species, size, condition, location and classification as a Protected Tree. (b) Required Submittals. To evaluate the existing trees the landscape plan and a tree evaluation schedule shall be submitted with the planning application showing: (1) The location of all existing trees six (6) inches or greater in trunk diameter (measured at 54 inches from natural grade), noting which are to be removed and which are located within the allowable building area; (2) Trunk diameter in inches measured 54 inches above natural grade; (3) Species name and species value as determined by utilizing the most recent edition of the Guide for Plant Appraisal, published by the Council of Tree and Landscape Appraisers; (4) Condition and location value of trees as determined by an ISA Certified Arborist; (5) The total LU value of trees to be removed; and (6) The total LU value of replacement trees. (c) Landscape Unit Value (LU). (1) The tree species, condition, and location values of the trees shall be based on an evaluation by an experienced landscape appraiser recognized by the American Society of Consulting Arborists utilizing the most recent Guide for Plant Appraisal, published by the Council of Tree and Landscape Appraisers; and approved by the Zoning Administrator. (2) Trees not within the allowable building area shall receive a location factor of 1.0 (100%). Trees located within the allowable building area shall receive a location factor of .70 (70%). (3) Trees designated as heritage trees shall receive a bonus percentage value of 1.25 (125%). Trees located within the allowable building area shall receive a location factor of .70 (70%). (4) Trees designated as heritage trees shall receive a bonus percentage value of 1.25 (125%). The species, condition and location value assume an average tree value to be .70 (.7 x .7 x .7 = .343). All existing trees to be removed shall be given a LU value based upon the following calculation: (d) Tree Replacement. Existing trees to be removed shall be replaced with new trees to equal the total removed LU value. The following rates shall be given to replacement trees to obtain the replacement LU value: The LU value for replacement Street Trees shall be calculated separately from other replacement trees. (e) Preservation of Heritage Trees. The site design shall make every reasonable effort to preserve Heritage Trees, consistent with Chapter 13.40. Conditions shall also be imposed to protect Heritage Trees during construction. Heritage Trees shall be removed only when the City Arborist determines that their preservation would result in a threat to health, safety, and welfare due to a hazardous tree condition, impacts on soil erosion and stability, or an unreasonable effect upon the economic enjoyment of the property, consistent with Chapter 13.40. (f) Protection of Existing Trees. The site design shall make reasonable effort to protect existing trees. The design shall be evaluated as to how it protects existing trees or the reasons for removal of existing trees. Tree protection measures shall be provided for trees to remain on-site, which shall be consistent with Chapter 13.40 and imposed as a condition of approvals. (g) Alternates to On-Site Replacement. If the required LU value for replacement of existing trees to be removed is not made up with replacement trees on-site, the City shall require that trees be planted in another location on-site or off-site or a contribution of funds be made to the City to be used for plantings on public land or a combination of the above options. If a contribution of funds is required, it shall be the fee as established by resolution of the City Council in the annual Comprehensive Fee Schedule."
    }
  ],
  "Chapter 27.72 NONCONFORMING BUILDINGS AND USES": [
    {
      "heading": "27.72.010 CONTINUANCE OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.72.010",
      "text": "(a) Any lawfully established use of a building or land, existing at the effective date of this title, or of amendments thereto, that does not conform to the use regulations for the district in which it is located, shall be deemed to be a legal nonconforming use and may be continued, except as otherwise provided herein. (b) Any legal nonconforming building or structure may be continued in use provided there is no physical change other than necessary maintenance and repair, except as otherwise permitted herein. (c) Any building for which a building permit has been lawfully granted prior to the effective date of this title, or of amendments thereto, may be completed in accordance with the approved plans; provided construction is started within sixty days of the date of the building permit and diligently prosecuted to completion. Such building shall thereafter be deemed a lawfully established building. This subsection is not intended to extend the effective time of any building permit granted pursuant to this code, or any ordinance, rule or regulation of the City."
    },
    {
      "heading": "27.72.020 DISCONTINUANCE OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.72.020",
      "text": "(a) Whenever any part of a building, structure or land occupied by a nonconforming use is changed to or replaced by a use conforming to the provisions of this title, such premises shall not thereafter be used or occupied by a nonconforming use, even though the building may have been originally designed and constructed for the prior nonconforming use. (b) Whenever a nonconforming use of a building or structure, or part thereof, has been discontinued for a period of six consecutive months, such use shall not after being discontinued or abandoned be reestablished, and the use of the premises thereafter shall be in conformity with the regulations of the district. (c) Where no enclosed building is involved, discontinuance of a nonconforming use for a period of six months constitutes abandonment, and the use of such premises shall thereafter conform with the regulations of the district and shall not thereafter be used in a nonconforming manner. (d) A nonconforming use not authorized by the provisions of this code and amendments thereto in effect at the time this title becomes effective, shall be discontinued and not reestablished unless, pursuant to the provisions of this title, the use is conforming to the district in which it is then located."
    },
    {
      "heading": "27.72.030 POWER TO ESTABLISH.",
      "id": "/us/ca/cities/san-mateo/code/27.72.030",
      "text": "Upon application of any property owner, or by action initiated by the commission or council, premises within the City may be ascertained and established as a nonconforming use in the manner herein provided."
    },
    {
      "heading": "27.72.040 CHANGE OF NONCONFORMING USE.",
      "id": "/us/ca/cities/san-mateo/code/27.72.040",
      "text": "(a) Use of Nonconforming Building. The nonconforming use of any building, structure, or portion thereof, which is designed or intended for a use not permitted in the district in which it is located, may be changed to another nonconforming use thereof under the procedure provided for obtaining a special use permit under Chapters 27.06 through 27.12, 27.62, 27.74, 27.78 and 27.80. (b) When any land has been devoted to a nonconforming use, permitted by this code, and the Council, after due notice and lawful hearing thereon, has found and determined that fifty percent or more replacement value of the building or buildings located thereon has become dangerous or injurious to the public health, safety or welfare, by reason of dilapidation, neglect, decay or otherwise, such use shall forthwith revert back to the classification to which it formed an exception, without further hearing or action thereon."
    },
    {
      "heading": "27.72.050 TERMINATION AND REMOVAL OF NON-CONFORMING USES OF LAND.",
      "id": "/us/ca/cities/san-mateo/code/27.72.050",
      "text": "A non-conforming use of land herein shall be terminated within such period as specified by the Council, but not less than two years nor more than five years where the Council determines that such use is especially burdensome upon the surrounding neighborhood or the community at large and that a termination within such time will not be unduly oppressive or constitute a denial of constitutionally guaranteed rights. In considering whether a particular use is of such nature, the following factors shall be considered: (1) Whether said use causes or contributes to impairment of property values or economic stability of the surrounding area; (2) Whether said use is inhibitive of the type of development in the surrounding contemplated by the general plan and this code; (3) Whether said use is otherwise detrimental to the public health, safety and general welfare; (4) The usability of the land or the improvements for purposes permitted in the applicable zoning district; (5) The amount of hardship, if any, to the user of the land, which would be caused by such termination. The above factors shall also be considered in the determination of the amount of time to be allowed for termination."
    },
    {
      "heading": "27.72.052 HEARINGS; PROCEDURE.",
      "id": "/us/ca/cities/san-mateo/code/27.72.052",
      "text": "(a) Hearings. The planning commission and the City Council shall hold hearings pursuant hereto for the purpose of determining whether a use is especially burdensome within the meaning of Section 27.72.050 hereof and if so, the amount of time to be allowed for continuance prior to termination. The procedure herein may be initiated by any councilman, planning commissioner or by the zoning administrator. (b) Procedure. The commission and council shall each hold at least one public hearing, notice of the nature, purpose, time and place of which shall be given to the owner and occupant of the property in question by mail at least ten days in advance of the date of hearing. Said notice shall also be published and posted in the manner prescribed in Section 27.08.090 of this code. At the time and place set for hearings the commission or council as the case may be shall proceed to hear all persons interested in the matter. In the case of the commission, its decision shall be recommendatory to the Council. The decision of the Council shall be final."
    },
    {
      "heading": "27.72.060 REPAIRS—ALTERATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.72.060",
      "text": "(a) Normal maintenance of a building or other structure containing a nonconforming use is permitted, including necessary nonstructural repairs and incidental alterations which do not extend or intensify the nonconforming use. (b) No structural alteration shall be made in a building or other structure containing a nonconforming use, except in the following situations: (1) When the alteration is required by law; (2) When the alteration will result in eliminating the nonconforming use; (3) When a building containing residential nonconforming uses may be altered in any way to improve livability, provided no structural alteration shall be made which would increase the number of dwelling units or the bulk of the building."
    },
    {
      "heading": "27.72.070 DAMAGE—DESTRUCTION.",
      "id": "/us/ca/cities/san-mateo/code/27.72.070",
      "text": "(a) If a building or other structure containing a nonconforming use is damaged or destroyed by any means to an extent of fifty percent or more of its replacement value at that time, as determined by the zoning administrator based upon current construction costs, the building or other structure can be rebuilt or used thereafter only for a conforming use and in compliance with the provisions of the district. In the event the damage or destruction is less than fifty percent of its replacement value, based upon prevailing construction costs, the building may then be restored to its original condition and the occupancy use of such building which existed at the time of such partial destruction may be continued. In either event, restoration or repair of the building or other structure must be started within a period of six months from the date of damage or destruction and diligently prosecuted to completion. (b) The provisions of subsection (a) shall not apply to the following: (1) Residential structures in residential districts; (2) Buildings in commercial, or office districts; and (3) Buildings in Transit Oriented Development (TOD) districts. In the event of partial or total damage or destruction thereto, all of the above structures in the listed zones may be restored to their original size, shape, volume and condition, and the use of such structures which existed at the time the damage or destruction occurred may be continued."
    },
    {
      "heading": "27.72.080 ADDITIONS—ENLARGEMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.72.080",
      "text": "(a) A nonconforming building may be enlarged or extended only if the entire building is thereafter devoted to a conforming use, and is made to conform to all the regulations of the district in which it is located. (b) No building partially occupied by a nonconforming use shall be altered in such a way as to permit the enlargement or expansion of the space occupied by such nonconforming use. (c) No nonconforming use may be enlarged or extended in such a way as to occupy any required usable open space, or any land beyond the boundaries of the zoning plot as it existed at the effective date of this title, or to displace any conforming use in the same building or on the same parcel. (d) A building or structure which is nonconforming with respect to yards, floor area ratio, or any other element of bulk regulated by this title may be altered to expand the interior floor area but shall not increase the degree or extent of its nonconformity with respect to the bulk regulations for the district in which it is located."
    },
    {
      "heading": "27.72.090 EXEMPTED BUILDINGS, STRUCTURES AND USES.",
      "id": "/us/ca/cities/san-mateo/code/27.72.090",
      "text": "Wherever a lawfully existing building or other structure otherwise conforms to the use regulations of this title, but is nonconforming only in the particular manner hereinafter specified, the building and use thereof shall be exempt from the requirements of Section 27.72.060: (1) In any R district, where a building is nonconforming only as to the number of dwelling units it contains, provided no such building shall be altered in any way so as to increase the number of dwelling units therein; (2) In any R district, where a use permitted in the C1 district occupies ground floor space within a multiple family dwelling located on a corner lot; (3) In any C or M district, where the use is less distant from an R district than that specified in the regulations for the district in which it is located; (4) In any district, where an established building, structure or use is nonconforming with respect to the standards prescribed in this chapter for any of the following: (A) Floor area ratio, (B) Yards, front, side, or rear, (C) Off-street parking or loading, (D) Lot area, (E) Gross floor area, (F) Garages or carports, (G) Lot coverage."
    },
    {
      "heading": "27.72.100 CONVERSION TO SPECIAL USE.",
      "id": "/us/ca/cities/san-mateo/code/27.72.100",
      "text": "Any nonconforming use may be made a special use by the granting of a special use permit as authorized by Chapter 27.74."
    }
  ],
  "Chapter 27.73 TC DISTRICT—TRANSPORTATION CORRIDOR SECTIONS": [
    {
      "heading": "27.73.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.73.010",
      "text": "The Transportation Corridor (TC) district is established to maintain adequate public transportation corridors to accommodate highway and rail transit at US 101, SR 92, and the rail line. It is intended to protect these corridors from encroaching development which might interfere with the transportation use or create a hazardous condition."
    },
    {
      "heading": "27.73.020 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.73.020",
      "text": "The following uses are permitted: (a) Railroad rights-of-way and improvements, (b) Freeway rights-of-way and improvements, (c) Public Utilities, (d) Public transit stations, such as, but not limited to railroad stations and bus terminals, (e) Accessory uses directly related to and necessary for the operations and maintenance of any permitted use, (f) Minor and incidental retail and service uses designed exclusively for the use of public transit passengers at an authorized transit station, (g) Park and Ride lots established by the State of California Department of Transportation or by an authorized local authority, and (h) Accessory parking lots serving transit stations."
    },
    {
      "heading": "27.73.030 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.73.030",
      "text": "(a) Accessory parking lots for abutting commercial uses, when such area is not required for transportation operators. (Ord. 1990-18 § 1, 1990). (b) Automobile storage for off-site automobile dealerships, when such area is not required for transportation operators. This does not include sales, maintenance or other automobile related uses."
    },
    {
      "heading": "27.73.040 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.73.040",
      "text": "(a) All transportation corridors shall be maintained free of nuisances as defined by the City of San Mateo Municipal Code, (b) No uses shall be allowed, as either permitted or special uses, where such uses will impede upon the operation of transportation corridors for transportation purposes."
    }
  ],
  "Chapter 27.74 SPECIAL USE PERMITS": [
    {
      "heading": "27.74.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.74.010",
      "text": "The formulation and enactment of a comprehensive zoning code is based on the division of the entire City into districts in each of which are permitted specified uses that are mutually compatible. In addition to such permitted compatible uses, however, it is recognized that there are other uses which it may be necessary or desirable to allow in a given district but which on account of their potential influence upon neighboring uses or public facilities need to be carefully regulated with respect to location or operation for the protection of the community. Such uses are classified in this title as \"special uses\" and fall into three (3) categories: (1) Use either municipally operated or operated by publicly regulated utilities or uses traditionally affected by public interest; (2) Uses entirely private in character which, on account of their peculiar locational need, the nature of the service they offer to the public, and their possibly damaging influence on the neighborhood, may be established in a district or districts in which they cannot reasonably be allowed as an unrestricted permitted use under the zoning regulations; and (3) Nonconforming uses which as special use permits can be made more compatible with their surroundings."
    },
    {
      "heading": "27.74.020 POWER TO GRANT.",
      "id": "/us/ca/cities/san-mateo/code/27.74.020",
      "text": "Power to grant a special use permit shall be limited to those uses designated as \"special use\" within the districts established under this title. Other nondesignated uses which the Planning Commission concludes are so similar to any specifically allowed use in the district as to be virtually identical thereto in terms of impact and land use requirements may also be allowed as special uses. The appropriate approval body shall have the power to hear evidence that the granting of such permit will or will not adversely affect the general health, safety and/or welfare of the community, and that the use, if permitted, will not cause injury or disturbance to adjacent property traffic or by excessive noise, smoke, odor or noxious gas, dust, glare, heat or fumes, or industrial waste. Any physical alteration, physical expansion, or change of an existing approved special use shall require a review by and be final with the Planning Commission, unless appealed to the City Council in accordance with Section 27.08.060. Any use designated as a \"special use,\" but which does not currently have a special use permit, shall be required to procure a special use permit from the appropriate approval body for any physical alteration, physical expansion, or change of the use."
    },
    {
      "heading": "27.74.025 LAPSE FOR DISCONTINUANCE OF A SPECIAL USE.",
      "id": "/us/ca/cities/san-mateo/code/27.74.025",
      "text": "If a special use for which a special use permit has been granted is discontinued for one (1) year, the permit shall become null and void. After a special use permit becomes null and void, use of the premises shall be restricted to those permitted uses in the zoning district."
    },
    {
      "heading": "27.74.030 TEMPORARY USE PERMIT.",
      "id": "/us/ca/cities/san-mateo/code/27.74.030",
      "text": "(a) Permitted Uses. A temporary use permit may be granted by the Zoning Administrator for uses not intended to become permanent, and which are either permitted in the district where the site is located, or permitted by this section. (b) Zoning Administrator. The Zoning Administrator shall have final decisional authority, subject to approval for uses occurring on private property which do not exceed a duration of 30 calendar days. The uses may include, but are not limited to, the following types of outdoor uses: promotional activities, sales, or storage structures, and amusement facilities. (c) The Zoning Administrator may also approve extensions up to six (6) months for each approved temporary use permit."
    },
    {
      "heading": "27.74.040 TEMPORARY USE PERMIT ISSUANCE APPROVAL.",
      "id": "/us/ca/cities/san-mateo/code/27.74.040",
      "text": "(a) The Zoning Administrator shall consider the proposed location of the temporary use and its probable effect on the surrounding neighborhood. To protect the public welfare, the Zoning Administrator may deny any application for a temporary use permit, or may grant such a permit subject to conditions. Such conditions may relate, among other things, to provisions for traffic circulation, parking, lighting, security, fire protection, noise and pollution control. Time limits less than 30 days may be attached to the use permit. (b) Violation of any condition imposed on any temporary use permit shall be grounds for its revocation by the Zoning Administrator. No temporary use permit shall be granted for any use which overburdens the City's public services, or which will place an unreasonable burden on nearby properties or residents."
    },
    {
      "heading": "27.74.050 TEMPORARY USE PERMIT PROCEDURES.",
      "id": "/us/ca/cities/san-mateo/code/27.74.050",
      "text": "Applications for temporary use permits shall be processed in a manner similar to that for other special use permits. The required submittal documents and fees shall be as specified by resolutions adopted by the Council from time to time."
    }
  ],
  "Chapter 27.75 MIXED USE CONVENIENCE MARKET/AUTOMOBILE SERVICE STATIONS": [
    {
      "heading": "27.75.010 INTENT.",
      "id": "/us/ca/cities/san-mateo/code/27.75.010",
      "text": "The intent of this chapter is to regulate the design and operation of Mixed Use Convenience Market/Automobile Service Stations."
    },
    {
      "heading": "27.75.020 MIXED USE CONVENIENCE MARKET/AUTOMOBILE SERVICE STATION: SPECIAL USE PERMIT REQUIRED.",
      "id": "/us/ca/cities/san-mateo/code/27.75.020",
      "text": "No mixed use convenience market/automobile service station may be operated in the City except pursuant to a special use permit granted by the Planning Commission in accordance with this chapter. An application for such a special use permit may be filed for any property which is zoned to allow an automobile service station, either as a permitted or a special use."
    },
    {
      "heading": "27.75.030 PROCEDURE.",
      "id": "/us/ca/cities/san-mateo/code/27.75.030",
      "text": "The Planning Commission review and decision on an application for a special use permit for a mixed use convenience market/automobile service station shall be subject to the following: (a) Procedural requirements for the processing of a planning application contained in Title 27 of this Code, including but not limited to the requirements for notice in section 27.08.050, and an appeal in section 27.08.090. (b) Written findings, as set forth in Chapter 27.74 of this code (special use permits) and, in addition, finding that the location of the mixed use convenience market/automobile service station will not have a detrimental effect on abutting residential districts. The findings shall be based on substantial evidence in view of the whole record."
    },
    {
      "heading": "27.75.040 TRANSITIONAL YARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.75.040",
      "text": "All mixed use convenience market/automobile service stations shall be separated from residential districts by at least one hundred (100) feet, measured from parcel line to parcel line."
    },
    {
      "heading": "27.75.050 TWELVE (12) MONTH REVIEW.",
      "id": "/us/ca/cities/san-mateo/code/27.75.050",
      "text": "Any approved Special Use Permit for a mixed use convenience market/automobile service station shall be reviewed once by the Planning Commission within twelve (12) months of the commencement of the mixed use operation. As a result of this review the Commission may modify or revoke the Special Permit upon finding that the use is being conducted in a manner adverse to the general health, safety and welfare of the community, and is causing injury or disturbance to adjacent properties by traffic, excessive noise, glare or litter."
    },
    {
      "heading": "27.75.060 DESIGN REVIEW STANDARDS FOR SERVICE STATIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.75.060",
      "text": "All newly constructed convenience market/automobile service stations shall comply with the provisions of Chapter 27.77 [Design Review Standards for Service Stations]. Remodeling of an existing gas stations to add a convenience market shall not increase the nonconformity in the existing improvements or landscaping. Conditions of approval may be imposed requiring existing landscaping and structures to be upgraded to meet the requirements of Chapter 27.77."
    },
    {
      "heading": "27.75.070 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.75.070",
      "text": "The following conditions shall apply to all Special Use Permits for mixed use convenience market/automobile service station: (a) A litter control plan shall be submitted with an application. The litter control plan shall indicate the location of trash receptacles and provisions for employee maintenance of the site. (b) The hours of operation for the convenience market shall be established by Special Permit with consideration of the potential impacts upon adjacent residential areas. (c) There shall be at least one (1) qualified attendant on duty while the automobile service station is open. Qualification shall be established to the satisfaction of the Fire Marshal or authorized representative prior to occupancy and shall include such factors as ability to supervise, observe and control the dispensing of flammable or combustible liquids into the fuel tank of motor vehicles or approved container, knowledge of the location and in the operation of fire extinguishers, ability to control sources of ignition and give immediate attention to accidental spills, if needed, in accord with Article 79 of the Uniform Fire Code. (d) The operation shall provide an on-premise silent alarm system connected to an approved central station or direct hook-up to the Communications Center at the San Mateo Police Department. (e) A crime prevention program, subject to approval of the Police Department, shall be submitted with an application. (f) The following shall apply to the sale of alcohol: (1) No alcoholic beverages shall be displayed within five feet of the cash register or the front door unless it is in a permanently affixed cooler. (2) No sale of alcoholic beverages shall be made from a drive-in window. (3) No display or sale of alcoholic beverages shall be made from an ice tub. (4) No alcoholic beverages advertising shall be located on motor fuel islands and no self-illuminated advertising for alcoholic beverages shall be located on buildings or windows. (5) Employees on duty between the hours of 10 p.m. and 2 a.m. shall be at least 21 years of age if alcoholic beverages are to be sold during those hours. (6) On-sale alcoholic beverages shall be prohibited; no consumption of alcohol shall occur on site."
    }
  ],
  "Chapter 27.76 PERFORMANCE STANDARDS": [
    {
      "heading": "27.76.010 METHOD OF COMPUTING NET RATE OF EMISSION OF PARTICULATE MATTER.",
      "id": "/us/ca/cities/san-mateo/code/27.76.010",
      "text": "The rate of emission of particulate matter from all sources within the boundaries of any lot shall not exceed the net figure in pounds per acre of lot area prescribed in the regulations for the manufacturing district in which the lot is located after deducting from the gross hourly emission per acre the correction factors set forth in the appropriate tables incorporated hereafter for height, velocity and temperature of emission. The method for determining the total net rate of emission of particulate matter within the boundaries of any lot shall be as follows: (1) Determine the maximum emission in pounds per hour from each source of emission within the lot boundaries and divide each figure by the number of acres of lot area, thereby obtaining the gross hourly rate of emission in pounds per acre for each source of emission; (2) From each gross hourly rate of emission derived in (1), deduct the appropriate correction factor (interpolating as required) for height, velocity, and temperature of emission as set forth in the tables which follow, in Sections 27.76.020 through 27.76.040, thereby obtaining the net rate of emission in pounds per acre of lot area for each source of emission; (3) Add together the individual net rate of emission derived in (2), to obtain the total net rate of emission within the boundaries of the lot. Such total shall not exceed the number of pounds per acre of lot area during any one hour prescribed as maximum for the district in which the lot is located."
    },
    {
      "heading": "27.76.020 ALLOWANCE FOR HEIGHT OF EMISSION.",
      "id": "/us/ca/cities/san-mateo/code/27.76.020",
      "text": ""
    },
    {
      "heading": "27.76.030 ALLOWANCE FOR VELOCITY OF EMISSION.",
      "id": "/us/ca/cities/san-mateo/code/27.76.030",
      "text": "Particulate matter correction in pounds per hour per acre."
    },
    {
      "heading": "27.76.040 ALLOWANCE FOR TEMPERATURE OF EMISSION.",
      "id": "/us/ca/cities/san-mateo/code/27.76.040",
      "text": "Particulate matter correction in pounds per hour per acre."
    },
    {
      "heading": "27.76.050 EXPLOSIVES.",
      "id": "/us/ca/cities/san-mateo/code/27.76.050",
      "text": "For the purposes of this title, the list of materials or products which decompose by detonation includes, but is not limited to, the following: (1) Acetylides; (2) Azides; (3) Chlorates; (4) Dynamite; (5) Blasting gelatin; (6) Fulminates; (7) Anhydrous hydrazine; (8) Ammonium nitrate; (9) Dinitroresorcinol; (10) Dinitrotoluene; (11) Guanidine nitrate; (12) Guncotton (cellulose nitrate of pyroxylin); (13) Hexamine; (14) Nitroglycerin; (15) Petn. (pentaerythritoltetranitrate); (16) Picric acid; (17) Tetryl (trinitrophenylmethyltramine); (18) Cylonite or hexogen (trimethylene trinitramine); (19) Dinol; (20) Petryl; (21) TNT (trinitrotoluene); (22) Perchlorates (when mixed with carbonaceous materials); (23) Black powder; (24) Fireworks; (25) Greek fire; (26) Permanganates; (27) Peroxides."
    }
  ],
  "Chapter 27.77 DESIGN REVIEW STANDARDS FOR SERVICE STATIONS": [
    {
      "heading": "27.77.010 INTENT.",
      "id": "/us/ca/cities/san-mateo/code/27.77.010",
      "text": "It is the intent of the following planning policy to insure that all service stations in the City of San Mateo be constructed and operated in a manner appropriate to the various districts and without detriment to the appearance of the immediate vicinity and to the City as a whole. This policy is intended to represent minimum standards of aesthetic suitability and to establish minimum standards for development of service stations in the City of San Mateo. Meeting these design review standards shall not be construed as a sole justification for the granting of a special permit. All other requirements of the zoning ordinance must be met for review and consideration by the Planning Commission. Any action by the Planning Commission is subject to review by the City Council."
    },
    {
      "heading": "27.77.020 DESIGN REVIEW STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.77.020",
      "text": "(a) Location. (1) Not more than two (2) service stations shall be located on any given street intersection, unless a finding is made that the general health, safety and/or welfare of the community will not be adversely affected and that the use will not cause injury or disturbance to adjacent property by traffic, noise, or otherwise. (2) At new service stations there shall be a minimum setback of 15 feet from any right of way for any gasoline pump island. (3) The use of service station driveways shall be designed to discourage use by adjacent shopping center traffic. (4) Off-street access points between the service station and an adjacent shopping center shall be provided. (5) Grease bays shall face away from any street if feasible as determined by the Zoning Administrator."
    },
    {
      "heading": "27.77.030 ACCESSORY USES AND MERCHANDISING.",
      "id": "/us/ca/cities/san-mateo/code/27.77.030",
      "text": "(a) All business shall be conducted within a completely enclosed building, except for service to automobiles normally conducted at the pump islands and other designated service areas. Minor automotive repair, washing and lubrication operations shall not take place outside the building. Major body work is not permitted as an accessory use. Lubricating oil cabinets and like accessory items may be located on, or adjacent to, each pump island. (b) Storage of travel trailers, rental trailers, car rentals, garden supplies and other similar uses of a storage or sales nature not permitted as a primary use in the zoning district in question shall not be allowed as an accessory use to the service station. (c) All retail merchandise shall be stored within the building including tires, mufflers or similar merchandise. (d) All hazardous and toxic waste shall be disposed of in accordance with County of San Mateo Health Department regulations. (e) Only vehicles awaiting service shall be permitted to be stored on the premises, with the exception of employee or customer parking, and rental parking utilizing spaces other than those required by chapter 27.64. (f) Parking of commercial vehicles shall be prohibited unless allowed in the zoning district as a permitted use. (g) Restrooms shall be provided for all service station customers."
    },
    {
      "heading": "27.77.040 LOT AREA.",
      "id": "/us/ca/cities/san-mateo/code/27.77.040",
      "text": "Every service station erected on a zoning plot not formerly used as a service station shall be required to have a minimum lot area of 20,000 square feet unless a finding is made that the general health, safety and/or welfare of the community will not be adversely affected and that the use will not cause injury or disturbance to adjacent property by traffic, noise, or otherwise."
    },
    {
      "heading": "27.77.050 LANDSCAPING.",
      "id": "/us/ca/cities/san-mateo/code/27.77.050",
      "text": "(a) Landscaping shall be provided as follows: (1) A four-foot minimum width landscaped strip along all street frontages, except for necessary driveways. (2) A raised curb of at least six inches in height, or a raised planter, shall be provided along all of the street property lines except for driveway openings. (3) The triangular corner area between driveways near the intersection shall be planted. Such plant materials shall not exceed 30 inches in height, excepting trees trimmed to the trunk for a height of 8 feet above the top of the nearest curb or pavement edge. (4) A solid wall or solid fence shall be provided between the station plot and any adjacent residential district. The wall or fence shall be 6 feet in height except within 25 feet of a street intersection line, the height in this area to be 3 feet. (5) Not less than ten percent of the lot area must be devoted to landscaping. Above stated items are included in this percentages. (6) Permanent irrigation facilities shall be provided for all landscaping. (7) Landscaping shall conform with the City's development landscape regulations."
    }
  ],
  "Chapter 27.78 VARIANCES": [
    {
      "heading": "27.78.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.78.010",
      "text": "In order that the purpose of this Code may be carried out, the approval body designated in this Title may, upon receiving an application for a variance from the provisions of this Title, vary such provisions upon finding that owing to special conditions, enforcement of the Title would result in hardship. Any variance granted shall be subject to such conditions as will assure that the adjustment authorized shall not constitute a grant of special privilege."
    },
    {
      "heading": "27.78.020 Conditions for Granting.",
      "id": "/us/ca/cities/san-mateo/code/27.78.020",
      "text": "(a) In order to make its determination that there is hardship, the approval body designated in this Title shall determine if each of the following conditions pertain: (1) There are exceptional or extraordinary circumstances or conditions applicable to the property that do not apply generally to property in the same zone or neighborhood including buildings of architectural or historical significance or of architectural interest as recognized by action of the City Council or another government agency. (2) A variance is necessary for the preservation and enjoyment of a substantial property right of the applicant possessed by other property owners in the same zone or neighborhood; (3) Granting of the variance will not be materially detrimental to the public health, safety or welfare or materially injurious to other property or improvements in the neighborhood in which the property is located; and (4) Granting of the variance will not adversely affect or be inconsistent with the general plan. (b) Parking stall dimension variances shall also meet all of the following limitations: (1) Handicapped stalls required by the State Architect's Handicapped Access Regulations are not eligible for this process. (2) The application must be based on constraints imposed by physical features of the site (such as slopes, Major Vegetation to be preserved as defined in Chapter 23.40, or Protected Trees as defined in Chapter 13.40), or existing structural improvements. No variance shall be granted for stall dimensions due to mere lack of space on the site to meet standard requirements for the project, nor for the sole purposes of design simplicity, reduced cost or other convenience of the applicant. (3) Variances for the width of stalls shall only be allowed for locating posts or stub walls in the very front or rear part of the stalls where they will not obstruct the swing of doors for passenger vehicles, or to allow continued use of established parking structures. (4) The application meets one or more of the following: (A) The variance is needed to continue using existing facilities; (B) No more than one dimension is to vary, and by not more than 1 foot width or 6 inches height or 2 feet length; (C) No more than 10% of all required stalls, or 3 stalls, whichever is greater, are to vary; (D) The total volume of each of the stalls will be at least 95% of the unvaried volume of height, width and depth combined."
    },
    {
      "heading": "27.78.030 IMPOSITION OF CONDITIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.78.030",
      "text": "The planning commission may impose such conditions and restrictions upon the premises benefited by a variance as may be necessary to prevent injurious effects therefrom upon other property in the neighborhood, and otherwise effectuate the provisions of this title."
    },
    {
      "heading": "27.78.040 AUTHORIZED VARIANCES.",
      "id": "/us/ca/cities/san-mateo/code/27.78.040",
      "text": "Variances from the regulations of this Title may be granted by the designated approval bodies only in accordance with the standards set forth in this chapter and may be granted in the following instances only: (a) To permit any yard of less dimension than required by the applicable regulations; (b) To permit a reduction of build-to-lines required by the applicable regulations; (c) To permit any building or structure to exceed the floor area ratio limitations imposed by the applicable regulations; (d) To permit the use of a zoning plot for a use otherwise prohibited solely because of the insufficient area of the lot, except that there shall be no increase in the number of units permitted on a site, nor shall there be permitted a density which exceeds the maximum allowable for each building site within each planning area as specified in Section 27.02.160 of this code and the housing element of the general plan; (e) To reduce the applicable off-street parking or loading facilities required or adjust stall dimensions; (f) To increase by not more than twenty-five percent the maximum distance that required parking spaces are permitted to be located from the use served; (g) To permit the same off-street parking facilities to qualify as a required facility for two or more uses, provided the substantial use of such facility by each use does not take place at approximately the same hours of the same days of the week."
    }
  ],
  "Chapter 27.79 REASONABLE ACCOMMODATION FOR RESIDENTIAL USES": [
    {
      "heading": "27.79.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.79.010",
      "text": "It is the policy of the City of San Mateo to provide persons with disabilities reasonable accommodation in regulations and procedures to ensure equal access to housing, and to facilitate the development of housing for persons with disabilities. This chapter is based on requirements of Federal and State housing laws, including the Federal Americans with Disabilities Act, the Federal Fair Housing Act and the California Fair Employment and Housing Act, and implements the housing element of the City's General Plan. The purpose of this chapter is to provide a procedure under which a person with disabilities may request a reasonable accommodation in the application of zoning regulations in order to secure equal access to housing, and outlines a process for decision makers to act upon such requests. This chapter is intended solely for residential use and is distinct from the requirements for a variance. The City also recognizes the importance of sustaining and enhancing residential neighborhoods, as articulated in the City's General Plan, and will consider whether the requested reasonable accommodation would result in an undue burden to the City or a fundamental alteration of City policies."
    },
    {
      "heading": "27.79.020 DEFINITIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.79.020",
      "text": "(a) \"Person with disabilities\" has the meaning set forth in the Federal Fair Housing Act and the California Fair Employment and Housing Act and is an individual who has a physical or mental impairment that limits one or more of the major life activities of such individual, is regarded as having such an impairment, or has a record of such impairment. (b) \"Reasonable accommodation\" means the act of making a dwelling unit or housing facility(ies) readily accessible to and usable by a person with disabilities, through the removal of constraints in the City's land use, zoning, permit and processing procedures."
    },
    {
      "heading": "27.79.030 APPLICABILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.79.030",
      "text": "The provisions of this chapter apply to residential uses that will be used by a person with disabilities. In order to make specific housing available to a person with disabilities, any person may request a reasonable accommodation, or exception to the City's zoning code regulations, in accordance with this chapter."
    },
    {
      "heading": "27.79.040 APPLICATION AND REVIEW PROCEDURE.",
      "id": "/us/ca/cities/san-mateo/code/27.79.040",
      "text": "(a) Applicant. Any person who requests reasonable accommodation, based on the disability of residents, in the application of a land use or zoning law which may be acting as a barrier to fair housing opportunities, must submit an application. The applicant may be the person with the disability, or his or her representative, or a developer of housing for people with disabilities. (b) Application. An application shall be filed with the Zoning Administrator, or designee, on a form provided by the Community Development Department. The application shall include all submittal requirements set forth below. No application fee will be charged. If assistance is needed to complete the application, or an alternative format for the application is necessary, the applicant shall contact the Zoning Administrator, or designee, for assistance. The applicant shall provide the following information: (1) Applicant's name and contact information; (2) Property address(es) and assessor's parcel number(s); (3) Property owner(s) name(s) and contact information; (4) Property owner(s) signature; (3) Current use of the property; (4) Basis for the claim, such as a medical certification, that the person on whose behalf the accommodation is sought is disabled; (5) Explanation of why the reasonable accommodation is necessary to make the specific housing accessible to the person with disabilities; (6) Plans showing the details of the proposal; (7) Other relevant information as requested by the Zoning Administrator, or designee, in order to make the required findings. These may include, but are not limited to: an arborist report (for tree removal as per Chapter 27.71 Landscape) and geotechnical report (for substantial grading as per Chapter 23.40 Site Development Code). For low income households (as defined in Health and Safety Code Section 50079.5), the City will fund the cost of any required technical reports so long as doing so would not constitute an \"undue financial burden\" (as provided in the Federal Regulations for Title II of the Americans with Disabilities Act) for the City. (c) If the project for which the request for reasonable accommodation is being made also requires another discretionary planning approval, the application for reasonable accommodation shall be submitted, reviewed, and noticed with the related planning application(s). (d) Public Notice. Within 10 days of deeming an application complete, a notice of pending application shall be sent to all property owners adjacent to the subject property. The notice shall include the following information: (1) Description of reasonable accommodation request; (2) Statement of the scope of application review permitted by this chapter; (3) Date by which public comments regarding the application must be submitted for consideration; (4) Date that the Zoning Administrator, or designee, shall make a determination on the application; and (5) Appeal rights. (e) Findings. Any decision on an application under this chapter shall be supported by written findings addressing the criteria set forth below. An application under this chapter for a reasonable accommodation shall be granted if all of the following findings are made: (1) The housing, which is the subject of the request, will be used by a person with disabilities. (2) Due to the physical attributes of the subject property or the structures on site, the requested reasonable accommodation is necessary to make the specific housing available to an individual with a disability under the Federal Fair Housing Act and the California Fair Employment and Housing Act. (3) The requested reasonable accommodation would not create an undue financial or administrative burden for the City. (4) The requested reasonable accommodation would not require a fundamental alteration in City's land use and zoning ordinances, programs or policies. In making this finding, the decision-making body may consider, but its consideration is not limited to, the following factors: (i) Whether the proposed changes to the subject property and structures, would adversely impact the health, safety or use of adjacent properties or the City right-of-way. (ii) Whether any reasonable alternatives have been identified that would provide an equivalent level of benefit without requiring a reasonable accommodation or exception to the City's applicable rules, standards and practices. (f) Conditions of Approval. In granting a request for reasonable accommodation, the reviewing authority may impose conditions to ensure that the reasonable accommodation complies with the findings required by this chapter. Conditions may also be imposed to ensure that any removable structures or physical design features that are constructed or installed in association with the reasonable accommodation be removed once those structures or physical design features are no longer necessary in order to accommodate a person with disabilities. The reviewing authority may require the recordation of the conditions of approval, or its equivalent. (g) Determination. Within 30 calendar days of deeming an application complete, the Zoning Administrator, or designee, shall approve, conditionally approve, or deny the application. (h) Expiration of Reasonable Accommodation Planning Permit. The reasonable accommodation planning permit is valid for two years from the date of approval unless a longer period is stated in the planning permit. If the applicant does not begin the work authorized by the permit by the expiration date, the permit shall expire. The applicant may request one two-year extension from the Zoning Administrator, or designee, provided that the written request for the extension is submitted to the Zoning Administrator no less than 60 calendar days prior to the expiration of the planning permit. Requests for extensions that involve another discretionary approval shall comply with Section 27.08.087, Planning Approval Extension."
    },
    {
      "heading": "27.79.050 APPEALS.",
      "id": "/us/ca/cities/san-mateo/code/27.79.050",
      "text": "Any decision of the Zoning Administrator, or designee, may be appealed by the applicant or another individual to the Planning Commission and thereafter to the City Council in accordance with Section 27.08.090, Appeals. If the applicant appeals, no appeal fee will be charged. If a person other than the applicant appeals, the appeal fee will be in the amount set by resolution of the City Council. The Planning Commission and City Council shall limit its consideration of the appeal to whether the reasonable accommodation meets the findings set forth in this chapter. The decision of the City Council is final. If an application for reasonable accommodation is filed concurrently with another planning application, the appeal procedures for the other planning approval, permit, or entitlement will control."
    }
  ],
  "Chapter 27.80 AMENDMENTS": [
    {
      "heading": "27.80.010 INITIATION.",
      "id": "/us/ca/cities/san-mateo/code/27.80.010",
      "text": "Amendments to this title may be initiated in the manner prescribed in Chapter 27.08 by the Planning Commission, or may be filed by: (a) The owners of 50% or more in area of all the property within the boundaries of the area proposed to be reclassified; or (b) The owner or owners of the area proposed to be reclassified. Each such application filed with the zoning administrator shall be verified under oath by at least one of the owners of property within the area proposed to be changed, attesting to the truth and correctness of all facts and information presented with the application."
    }
  ],
  "Chapter 27.82 MAPS—BOUNDARY LINES": [
    {
      "heading": "27.82.010 ZONING MAPS.",
      "id": "/us/ca/cities/san-mateo/code/27.82.010",
      "text": "The locations and boundaries of the zoning districts established herein are shown upon the zoning maps of the City on file in the office of the City Clerk, which, together with all amendments, notations, references and other information shown thereon, are hereby incorporated into and made a part of this code."
    },
    {
      "heading": "27.82.020 BOUNDARY LINES.",
      "id": "/us/ca/cities/san-mateo/code/27.82.020",
      "text": "Whenever any uncertainty exists as to the boundary of any zoning district as shown on the zoning maps incorporated herein, the following rules shall apply: (a) Where district boundary lies are indicated as following streets, alleys, or similar rights-of-way, they shall be construed as following the centerlines thereof; (b) Where district boundary lines are indicated as approximately following lot lines, such lot lines shall be construed to be such boundaries; (c) Where a lot or parcel held in one ownership which is incapable of being subdivided and is of record on the effective date of this title is divided by a \"district\" boundary line, the entire lot or parcel shall be construed to be within the \"district\" containing more than half the area of the lot or parcel, provided the property is developed as one unit. If the lot or parcel is divided into equal parts it shall be deemed to be in the most restricted district. This does not apply to unplatted or unmapped parcels. If an unplatted or unmapped parcel held in one ownership is divided by a district boundary line, the portions of the parcel shown on the zoning map shall be construed to be in the district in which they are shown on the zoning map; (d) Where a street shall hereafter have been vacated or abandoned and such street was, prior to the adoption hereof, the division line or boundary between two districts, the centerline of the vacated or abandoned street shall remain the boundary between districts unless otherwise determined by the City Council; (e) In case any uncertainty may exist as to the location of a boundary or boundaries of any district, and there is a dispute with reference hereto, the person or persons so disputing such boundary or boundaries shall file an appeal with the Planning Commission in compliance with the provisions and procedures set forth in Chapter 27.08."
    }
  ],
  "Chapter 27.83 SLOPE AND HILLSIDE DEVELOPMENT STANDARDS": [
    {
      "heading": "27.83.010 R1 AND R2 DISTRICTS.",
      "id": "/us/ca/cities/san-mateo/code/27.83.010",
      "text": "Subdivisions that result in new parcels with slopes of twenty-five (25%) percent or more are prohibited unless the following conditions are met: (a) The parcel contains contiguous area that is less than twenty-five (25%) percent slope which equals or exceeds the minimum required parcel size for the applicable zoning district, and (b) Any access-way to that portion of the site less than twenty-five (25%) percent slope must limit alteration of the visual character of the hillside and meet the requirements for maximum street and driveway slopes and blending of cut and fill to natural grade."
    },
    {
      "heading": "27.83.020 MULTIPLE FAMILY AND COMMERCIAL DISTRICTS.",
      "id": "/us/ca/cities/san-mateo/code/27.83.020",
      "text": "Only those areas of a site have existing slopes of less than twenty-five (25%) percent shall be considered in the calculation of allowable floor area and density limits."
    }
  ],
  "Chapter 27.84 FENCES, TREES AND HEDGES": [
    {
      "heading": "27.84.010 FENCES—HEIGHT LIMITATION.",
      "id": "/us/ca/cities/san-mateo/code/27.84.010",
      "text": "No fence, wall or similar structure exceeding six (6) feet in height shall be erected, constructed or maintained on a property line or within a required yard area as defined in Title 27, except in the following instances: (a) Street Yards. The maximum height within a front yard or street side yard, as defined in Title 27, shall be three (3) feet, except that: (1) Fence or wall posts not more than 12 inches wide may be 42 inches (three and one-half (3 1/2) feet) tall, and (2) Entry structures, such as trellises, over pedestrian gates may be eight (8) feet tall and not more than five (5) feet wide. (b) Street Intersections and Driveways. The maximum height of fences and hedges near street intersections and driveways shall be limited to three (3) feet when located: (1) Within the triangular area of private property formed by the extension of intersection curb lines, or pavement edge where no curb exists, and the diagonal line connecting the point on each of the two (2) streets at a distance of 45 feet back from the intersection, as illustrated hereafter, or (2) Within the triangular area of private property formed by lines 10 feet in length from the point of intersection of the edge of driveways on the subject property or adjacent properties and the edge of the sidewalk closest to the private property, as illustrated hereafter. (c) Side and Rear Property Line Fences. The maximum height along interior side or rear property line outside of required front or street side yards shall be eight (8) feet provided that: (1) A building permit, applied for by all property owners abutting the property line fence, is issued pursuant to Title 23, and (2) 50% percent of the fence above six (6) feet in height shall be open. Provisions (1) and (2) above shall not apply for single-family properties which are adjacent to a multi-family, commercial or industrial use, although a building permit pursuant to Title 23 shall be required."
    },
    {
      "heading": "27.84.015 FENCES—HEIGHT MEASUREMENT ON SLOPING LOTS.",
      "id": "/us/ca/cities/san-mateo/code/27.84.015",
      "text": "For the purposes of this title, where the elevation between two (2) adjacent lots is different, the measurement of fence or wall height is taken from ground level of the upper lot to the top of the fence, wall or post."
    },
    {
      "heading": "27.84.020 EXCEPTIONS.",
      "id": "/us/ca/cities/san-mateo/code/27.84.020",
      "text": "The Zoning Administrator may grant an exception to the height and location requirements for fences through submittal of a planning application as set forth in Chapter 27.08 of this title. The Zoning Administrator may approve or conditionally approve the exception if all of the following conditions apply: (a) The fence or wall height, location, design and landscaping are in scale and harmonious with the character of the neighborhood; (b) Granting of the exception will not be materially detrimental to the public health, safety or welfare or materially injurious to other property or improvements in the neighborhood in which the property is located, and shall not limit visibility of pedestrians, bicyclists, or motorists from streets, alleys or driveways; and (c) Granting of the exception will not adversely affect or be inconsistent with the general plan."
    },
    {
      "heading": "27.84.025 EXISTING FENCES.",
      "id": "/us/ca/cities/san-mateo/code/27.84.025",
      "text": "A fence, wall, or similar structure which has been constructed prior to June 7, 1993 shall be permitted without the need for permit approvals otherwise required by this Municipal Code, including permits under Title 27 and Title 23. Nothing herein shall be construed to authorize a fence, wall, or similar structure in violation of Section 27.84.010(b) or in violation of the City's nuisance laws if the City determines that a nuisance exists (excepting therefrom a nuisance based on the failure to obtain permit approvals)."
    },
    {
      "heading": "27.84.030 FENCES OR WALLS REQUIRED FOR COMMERCIAL OR MANUFACTURING DISTRICTS ABUTTING RESIDENTIAL DISTRICTS.",
      "id": "/us/ca/cities/san-mateo/code/27.84.030",
      "text": "A solid wall or solid fence at least six (6) feet in height shall be constructed along or within 10 feet of the parcel line or zone boundary lines to separate manufacturing and commercial districts and/or uses from abutting residential districts as follows: (1) Zone boundaries which coincide with rear parcel lines and which are not on a street shall be the location of the wall or fence; (2) Zone boundaries which coincide with side parcel lines shall be the location for the wall; (3) Zone boundaries on streets shall require the wall to be set back 10 feet from the parcel line of the nonresidential use and the area between the wall and the parcel line shall be landscaped and maintained; and (4) Zone boundaries on an alley shall require the wall on the parcel line along the alley; (5) This chapter shall not be deemed to set aside or reduce the requirements established for security fencing by either local, State, or Federal law; and (6) The Zoning Administrator may permit non-solid fences and fences to be located within 15 feet of a parcel line if it is found that it improves architectural compatibility with the surrounding area, or improves security surveillance."
    },
    {
      "heading": "27.84.040 FENCE OR HEDGE—BRANCH EXTENSION.",
      "id": "/us/ca/cities/san-mateo/code/27.84.040",
      "text": "No person shall permit branches or trees or shrubs to extend over any portion of the public sidewalk unless providing a minimum eight (8) foot vertical clearance. No person shall permit branches or trees or shrubs to extend over any portion of a public street unless providing a minimum 14-foot vertical clearance. No person shall permit branches or shrubs to extend over the sidewalk rendering the sidewalk width less than four (4) feet."
    },
    {
      "heading": "27.84.050 HEDGE OR TREE—SITE OBSTRUCTION.",
      "id": "/us/ca/cities/san-mateo/code/27.84.050",
      "text": "No person shall maintain hedges or other growth of like nature, of a height greater than three (3) feet, or maintain growth of a mature tree lower than seven (7) feet: (a) Within the triangular area of private property formed by the intersection right-of-way lines of two (2) streets as described in the illustrations below; or (b) Within the building setback line area of private property adjacent to any street or alley which by its nature and location constitutes an actual vehicular or pedestrian sight obstruction as determined by the Public Works Director; or (c) Within any street or alley right-of-way. "
    }
  ],
  "Chapter 27.85 DAY CARE CENTERS": [
    {
      "heading": "27.85.010 PURPOSE AND SCOPE.",
      "id": "/us/ca/cities/san-mateo/code/27.85.010",
      "text": "The purpose of this chapter is to establish standards for day care centers. This chapter shall apply to day care centers, whether new or expanding, as \"day care center\" is defined in Section 27.04.130. This chapter shall not apply to \"family day care home\" as defined in Section 27.04.130."
    },
    {
      "heading": "27.85.020 DAY CARE STANDARDS AND CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.85.020",
      "text": "The following standards shall apply to day care centers unless modified by a special use permit: (a) Off-street parking facilities for day care center employees and designated loading/unloading spaces shall meet the requirements of Chapter 27.64. (b) Any new or expanding day care center shall be located at least three hundred (300) feet from any other day care facility requiring a special use permit, except this requirement would not apply to nor be affected by centers located within a public or quasi-public facility. The 300 feet shall be measured from property lines along the street frontage, on both sides of the street, and in all directions from the property including around corners and across intersecting streets. (c) The following standards and conditions of use shall apply in residential zones: (1) No outdoor play equipment shall be located in required front or street-side yards. (2) Outdoor play areas shall be enclosed with a solid, six-foot high fence along property lines abutting residential uses. Chain-link fences with slats shall not be considered a solid fence. (3) No structural or decorative alterations are permitted that change the residential appearance of the building exterior. (4) Nighttime security lighting shall not be directed at neighboring properties and the light source shall be shielded from view off-site. (5) Days and hours of operation shall be limited to weekdays, between the 6:30 a.m. and 7:30 p.m. Extended days or hours may be approved by a special use permit. These hours may be altered only through approval of a special use permit. (6) No signage shall be permitted for day care centers in residential districts, notwithstanding the provisions of Chapter 25.20."
    }
  ],
  "Chapter 27.86 RECYCLING COLLECTION AREAS": [
    {
      "heading": "27.86.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.86.010",
      "text": "This chapter is intended to establish procedures and regulate the establishment of recycling collection areas in development projects."
    },
    {
      "heading": "27.86.020 SCOPE.",
      "id": "/us/ca/cities/san-mateo/code/27.86.020",
      "text": "For the purposes of this chapter a \"development project\" is defined as any habitable commercial, institutional, marina, recreational structure, or residential development having five or more living units, or single family residential projects where solid waste is collected and/or loaded in a common location serving five or more units. This chapter shall apply to the following \"development projects\": (a) Any new development project, or additions to existing development projects which individually or cumulatively add thirty percent or more floor area within a 12-month period. In cases where projects add thirty percent (30%) or more floor area to an existing development project, regulations for recycling collection areas shall apply to all uses and the entire development project. (b) To individual tenants within an existing development project occupied by multiple tenants in which tenant improvements individually or cumulatively add thirty percent (30%) or more to the floor area of the tenant's business within a 12-month period."
    },
    {
      "heading": "27.86.030 DEVELOPMENT STANDARDS.",
      "id": "/us/ca/cities/san-mateo/code/27.86.030",
      "text": "The following minimum development standards shall apply to all new recycling collection areas. (a) The design, construction, and location of recycling collection areas shall not conflict with local laws relating to fire, building, access, transportation, circulation or safety. (b) Outdoor recycling areas must have bins or containers that provide protection against adverse environmental conditions. (c) Adverse impacts such as noise, odor, vectors, or glare shall be mitigated through adequate separation, fencing, landscaping and maintenance. (d) Areas for recycling shall be adequate in capacity, number and distribution to serve the needs of the occupants' of the development project. Site design must include adequate space for recycling and garbage containers and access for recycling/garbage collection trucks. The recycling/garbage collection area enclosures shall be located on level ground. (e) Dimensions of the recycling collection area shall accommodate the number and type of containers needed for both garbage and recycling receptacles sufficient to meet the recycling needs of either the development project for new developments, or the individual tenant for expansion projects."
    },
    {
      "heading": "27.86.040 GUIDELINES.",
      "id": "/us/ca/cities/san-mateo/code/27.86.040",
      "text": "The City Council may adopt guidelines to assist in the implementation of this chapter."
    },
    {
      "heading": "27.86.050 REVIEW.",
      "id": "/us/ca/cities/san-mateo/code/27.86.050",
      "text": "Review for compliance with this chapter shall be made by the Zoning Administrator."
    }
  ],
  "Chapter 27.87 OUTDOOR RESTAURANT SEATING AND MERCHANDISE DISPLAY": [
    {
      "heading": "27.87.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.87.010",
      "text": "The purpose of this chapter is to regulate the use of public sidewalks for restaurant seating and the use of private property for outdoor display of merchandise accessory to existing businesses. This chapter is not intended to regulate outdoor restaurant seating on private property or the use of public right-of-way for street fairs or other events otherwise regulated under Section 17.08.120 of the Municipal Code."
    },
    {
      "heading": "27.87.020 REQUIREMENTS.",
      "id": "/us/ca/cities/san-mateo/code/27.87.020",
      "text": "(a) Restaurant Seating on Public Sidewalks. Restaurant seating located on public sidewalks (in the public right-of-way) are allowed in all zoning districts for legally permitted restaurants, subject to meeting the development standards and conditions listed below and approval of an encroachment permit from the Department of Public Works. Nothing is intended to prevent the placement of conditions on the encroachment permit as deemed appropriate. (b) Outdoor Merchandise Display. Outdoor display of merchandise accessory to an existing business which occupies a building is permitted on private property in Neighborhood Commercial (C1) and Central Business (CBD) Districts. Such display is not permitted in the public right-of-way."
    },
    {
      "heading": "27.87.030 DEVELOPMENT STANDARDS AND CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.87.030",
      "text": "(a) Restaurant Seating. Restaurant seating located on public sidewalks must meet the following standards and conditions of use: (1) Clearance. The physical extent of the seating encroachment must be located so as to permanently maintain a minimum sidewalk pedestrian through zone of four (4) feet, free and clear between: (A) the outer boundary of the seating area and any physical obstruction, such as light standards, parking meters, news racks, trees, curb or other barrier; and (B) the entryways or display window of adjacent businesses, unless authorized by the adjacent business. (2) Physical Delineation of Seating Area. The physical extent of the seating encroachment may be clearly delineated by physical means, which, if either required or voluntarily placed, shall be approved as part of the encroachment permit and designed to be decorative, durable, removable and minimize tripping hazards. (3) Other Limitations. Tables, seating and any approved physical barriers to delineate the seating area are the only items permitted to be located on the sidewalk. These items shall be removed from the public sidewalk at the close of business each day. Other items, such as busing stations, are not permitted on public sidewalks. (4) Liability Insurance. Applicants for restaurant seating on the public sidewalk shall provide liability insurance providing endorsements showing the City of San Mateo as additional insured on the policy, in an amount determined by the City Attorney's office. Encroachment permits issued under authority of this chapter shall be valid only during the term of liability insurance coverage. (5) Site Maintenance. Sidewalk seating areas shall be maintained free of litter, refuse and debris. The area shall be scrubbed and mopped to remove any food or drink stains on a daily basis. Such cleaning shall be performed in accordance with the City's Stormwater Management and Discharge Control Program, which prohibits any discharge other than stormwater into the stormwater drainage system. The applicant shall post maintenance security in a form and amount determined upon issuance of the encroachment permit. Failure to maintain the site shall be cause for termination of the encroachment permit. (6) Encroachment Fee. The applicant shall pay an annual fee in the amount set forth in the Comprehensive Fee Schedule. (b) Merchandise Display. Merchandise display on private property must meet the following standards: (1) Private Property. Outdoor merchandise display shall be maintained completely on private property in the immediate vicinity of the store entryway, such as in recessed entryways or along storefronts. (2) Accessibility. Merchandise display areas shall maintain accessibility requirements for the disabled."
    },
    {
      "heading": "27.87.040 OFF-STREET PARKING AND LOADING.",
      "id": "/us/ca/cities/san-mateo/code/27.87.040",
      "text": "Off-street parking and loading shall not be required for: (1) outdoor restaurant seating in the public right-of-way; and (2) outdoor merchandise display on private property."
    }
  ],
  "Chapter 27.88 BAY MEADOWS SPECIFIC PLAN": [
    {
      "heading": "27.88.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.88.010",
      "text": "The Bay Meadows Specific Plan District (BMSP) is established to assure that the Bay Meadows Race Tract, Practice Track, and Bar Area is developed in a comprehensively planned manner, compatible with adjacent residential neighborhoods and consistent with the City's quality of life goals."
    },
    {
      "heading": "27.88.020 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.88.020",
      "text": "Those uses which are permitted in the Bay Meadows Specific Plan are permitted."
    },
    {
      "heading": "27.88.030 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.88.030",
      "text": "Those uses specified as special uses in the Bay Meadows Specific Plan may be permitted subject to approval of a special use permit by the Planning Commission."
    },
    {
      "heading": "27.88.040 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.88.040",
      "text": "All uses in the BMSP District are subject to the conditions of use specified in the Bay Meadows Specific Plan, including but not limited to, off-street parking and loading, setbacks, building heights, and floor area ratio requirements."
    },
    {
      "heading": "27.88.050 RELATIONSHIP TO OTHER LAWS.",
      "id": "/us/ca/cities/san-mateo/code/27.88.050",
      "text": "The requirements of the San Mateo Zoning Code, including the development standards and condition of use of general application throughout the City, shall govern the development, use, and operation of property within the BMSP District, except as otherwise expressly provided in the Bay Meadows Specific Plan. All terms not otherwise defined in the Bay Meadows Specific Plan shall have the meaning set forth in the San Mateo City Zoning Code. Notwithstanding Section 27.02.040 (or any other provision of the San Mateo City Zoning Code), in the event of a conflict between the terms, conditions, requirements, or policies of the Bay Meadows Specific Plan and the San Mateo City Zoning Code, the Bay Meadows Specific Plan shall govern.\""
    }
  ],
  "Chapter 27.90 TOD DISTRICT—TRANSIT ORIENTED DEVELOPMENT": [
    {
      "heading": "27.90.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.90.010",
      "text": "The purpose of the Transit Oriented Development (TOD) district is to implement the San Mateo Rail Corridor Transit Oriented Development Plan (Rail Corridor Plan). The TOD policies of the Rail Corridor Plan encourage more intensive development within walking distance of transit stations. TOD is intended to provide for an integrated mix of land uses that support transit use through site design that enhances accessibility to stations and is supportive of pedestrian and bicycle use."
    },
    {
      "heading": "27.90.020 APPLICABILITY.",
      "id": "/us/ca/cities/san-mateo/code/27.90.020",
      "text": "The provisions of the TOD District apply to the two geographic zones delineated on the Rail Corridor Plan as the Hillsdale Station TOD zone and the Hayward Park Station TOD zone. All development shall be planned in a comprehensive manner to ensure the creation of transit oriented development that is consistent with the Rail Corridor Plan. The City may require the submittal of a Specific Plan or similar document to fulfill the requirements of this chapter."
    },
    {
      "heading": "27.90.030 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.90.030",
      "text": "Those uses which are permitted in the TOD areas as designated in the Rail Corridor Plan Land Use Plan (Chapter 5 Land Use and Zoning)."
    },
    {
      "heading": "27.90.040 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.90.040",
      "text": "Nondesignated uses which the Planning Commission concludes are so similar to any specifically permitted use as designated in the Rail Corridor Plan Land Use Plan so as to be virtually identical thereto in terms of impact and land use requirements may also be allowed as special uses, subject to review and approval as a Special Use Permit by the Planning Commission."
    },
    {
      "heading": "27.90.050 DEVELOPMENT GUIDELINES.",
      "id": "/us/ca/cities/san-mateo/code/27.90.050",
      "text": "All uses are subject to the development standards policies and guidelines specified in Rail Corridor Plan, including but not limited to, minimum and maximum unit density, off-street parking and loading, transportation demand management, setbacks, building heights, floor area ratio requirements and open space."
    },
    {
      "heading": "27.90.060 TRANSPORTATION DEMAND MANAGEMENT.",
      "id": "/us/ca/cities/san-mateo/code/27.90.060",
      "text": "All projects shall be consistent with the provisions of Rail Corridor Plan Chapter 7 (G) Transportation Demand Management (TDM), including participation in the Transportation Management Association (TMA). All planning application submittals shall include a trip reduction and parking management plan. This plan shall include recommended trip reduction and parking reduction measures. These recommendations shall include a definition of appropriate trip generation thresholds for the project. This requirement shall pertain to all projects which result in a net increase of 100 p.m. peak hours trips (before implementation of TDM measures) as calculated using coefficients contained in the latest edition of Trip Generation as published by the Institute of Transportation Engineers."
    },
    {
      "heading": "27.90.070 RELATIONSHIP TO OTHER LAWS.",
      "id": "/us/ca/cities/san-mateo/code/27.90.070",
      "text": "The requirements of the San Mateo Zoning Code, including the development standards and condition of use of general application throughout the City, shall govern the development, use, and operation of property within the Transit Oriented Development District, except as otherwise expressly provided in the Rail Corridor Plan. All terms not otherwise defined in the Rail Corridor Plan shall have the meaning set forth in the San Mateo City Zoning Code. Notwithstanding Section 27.02.040 (or any other provision of the San Mateo City Zoning Code), in the event of a conflict between the terms, conditions, requirements, or policies of the Rail Corridor Plan and the San Mateo City Zoning Code, the Rail Corridor Plan shall govern."
    }
  ],
  "Chapter 27.92 HILLSDALE STATION AREA PLAN": [
    {
      "heading": "27.92.010 PURPOSE.",
      "id": "/us/ca/cities/san-mateo/code/27.92.010",
      "text": "The Hillsdale Station Area Plan is established to assure that the area surrounding the Hillsdale Caltrain station is developed to support travel via transit, walking, and bicycling, through mixed-use and other transit-oriented forms of development around a relocated Hillsdale Caltrain station, resulting in convenient access to the relocated station for residents and visitors."
    },
    {
      "heading": "27.92.020 BOUNDARIES.",
      "id": "/us/ca/cities/san-mateo/code/27.92.020",
      "text": "The Hillsdale Station Area Plan boundaries are as shown on the map below: "
    },
    {
      "heading": "27.92.030 PERMITTED USES.",
      "id": "/us/ca/cities/san-mateo/code/27.92.030",
      "text": "Permitted uses in the Hillsdale Station Area are as detailed in the applicable zoning district of the San Mateo City Zoning Code."
    },
    {
      "heading": "27.92.040 SPECIAL USES.",
      "id": "/us/ca/cities/san-mateo/code/27.92.040",
      "text": "Those uses specified as special uses in the San Mateo City Zoning Code may be permitted subject to approval of a special use permit by the Planning Commission."
    },
    {
      "heading": "27.92.050 CONDITIONS OF USE.",
      "id": "/us/ca/cities/san-mateo/code/27.92.050",
      "text": "All uses in the Hillsdale Station Area are subject to the conditions of use specified in the Hillsdale Station Area Plan, including but not limited to, off-street parking and loading, setbacks, development guidelines, and streetscape standards."
    },
    {
      "heading": "27.92.060 RELATIONSHIP TO OTHER LAWS.",
      "id": "/us/ca/cities/san-mateo/code/27.92.060",
      "text": "The requirements of the San Mateo City Zoning Code, including the development standards and conditions of use of general application throughout the City, shall govern the development, use, and operation of property within the Hillsdale Station Area, except as otherwise expressly provided in the Hillsdale Station Area Plan. All terms not otherwise defined in the Hillsdale Station Area Plan shall have the meaning set forth in the San Mateo City Zoning Code. Notwithstanding Section 27.02.040 (or any other provision of the San Mateo City Zoning Code), in the event of a conflict between the terms, conditions, requirements, or policies of the Hillsdale Station Area Plan and the San Mateo City Zoning Code, the Hillsdale Station Area Plan shall govern."
    }
  ],
  "Chapter 27.94 Housing Opportunities Overlay District (H)": [
    {
      "heading": "27.94.005 Purpose",
      "id": "/us/ca/cities/san-mateo/code/27.94.005",
      "text": "The purpose of the Housing Opportunities Overlay District (H) is to establish by-right residential uses on sites identiﬁed to accommodate a portion of the housing need for lower income housing in the General Plan Housing Element, pursuant to Government Code Sections 65583.2(c) and (i). This chapter establishes minimum development requirements and procedures for reviewing and approval of the by-right residential development uses."
    },
    {
      "heading": "27.94.010 By-Right Residential Use Eligibility",
      "id": "/us/ca/cities/san-mateo/code/27.94.010",
      "text": "The following housing development projects are eligible for by-right approval. Housing development projects that are ineligible for by-right approval shall be subject to the requirements for residential development in the underlying zoning district. (a) Pursuant to Government Code Section 65583.2(c) and (h), housing development projects in which at least 20 percent of the units proposed are affordable to lower income households, as defined in Health and Safety Code Section 50079.5, and is a household whose income is equal to or less than eighty percent of the area median income, as published by the California Department of Housing and Community Development. The housing development project shall be allowed at the density allowed in the underlying zoning district and shall be allowed a minimum density of at least 30 dwelling units per acre. A \"housing development project\" shall have the same meaning as defined in Government Code Section 65589.5(h)(2)."
    },
    {
      "heading": "27.94.020 By-Right Residential Use Requirements",
      "id": "/us/ca/cities/san-mateo/code/27.94.020",
      "text": "(a) Site plan and architectural review approval is required under Chapter 27.08, Rules of Procedure. The Zoning Administrator shall be the approval authority for projects proposed pursuant to this chapter that comply with the City's Municipal Code and Objective Design Standards. The Zoning Administrator shall not exercise any discretion in the review process for such projects and their decision shall be final. (b) The site plan and architectural review shall not constitute a \"project\" for the purposes of Division 13 (commencing with Section 21000) of the Public Resources Code. (c) Any subdivision of the site shall be subject to all laws, including, but not limited to Title 26 of the City of San Mateo Municipal Code (Subdivisions). (d) Notwithstanding Section 27.94.010, the following objective development standards shall apply to housing development projects built pursuant to this chapter: (1) Development standards set forth in the underlying zoning district. (2) For a project within another overlay district, the development standards of the overlay district. (3) For development projects within an E2 Zoning District without an overlay district, the R4 development standards. (4) For development projects within a Specific Plan or within the TOD zoning district, the applicable development standards of the Specific Plan or TOD zoning district. (5) Objective Design Standards for multi-family and residential mixed-use projects as adopted by City Council resolution. (6) Applicable standard conditions of approval."
    }
  ]
}
output = transform_structure(results)
 # print(output)
with open("transformed_san_mateo_code_results.json", "w", encoding="utf-8") as f:
     json.dump(output, f, ensure_ascii=False, indent=4)